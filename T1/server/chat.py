import zmq
from server.chat_monitor import ChatMonitor
from threading import Thread

class Chat(Thread):
    def __init__(self, chatname):
        super(Chat, self).__init__()
        self.__name = chatname

        self.init_queues()
        self.init_monitor()

    def get_name(self):
        return self.__name

    def get_ports(self):
        return self.__port_from_client, self.__port_to_client

    def get_counter_users(self):
        return self.__monitor.get_counter_users() 

    def init_queues(self):
        #Fila de mensagens vindas dos clientes
        self.__from_client_context = zmq.Context()
        self.__from_client_mq = self.__from_client_context.socket(zmq.SUB)
        self.__port_from_client = self.__from_client_mq.bind_to_random_port(addr="tcp://*")
        self.__from_client_mq.setsockopt_string(zmq.SUBSCRIBE, "")

        #Fila de mensagens enviadas para os clientes
        self.__to_client_context = zmq.Context()
        self.__to_client_mq = self.__to_client_context.socket(zmq.PUB)
        self.__port_to_client = self.__to_client_mq.bind_to_random_port(addr="tcp://*")

        self.__messages_thread = Thread(target=self.waiting_message)

    def init_monitor(self):
        self.__monitor = ChatMonitor(self.__name, self.__from_client_mq.get_monitor_socket())
        self.__monitor_thread = Thread(target=self.__monitor.start_monitoring)

    def run(self):
        self.__monitor_thread.start()
        self.__messages_thread.start()
        print(f"{self.__name}\t|\tStarted")

        self.__messages_thread.join()
        self.__monitor_thread.join()
        self.__to_client_mq.close()
        self.__from_client_mq.close()

    def waiting_message(self):
        while True:
            message = self.__from_client_mq.recv_json()

            name_user, text_received = message["user"], message["message"]

            print(f"{self.__name}\t|\tReceived from {name_user}: {text_received}")

            self.__to_client_mq.send_json(message)
