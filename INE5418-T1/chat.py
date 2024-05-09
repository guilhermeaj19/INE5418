import zmq
from chat_monitor import ChatMonitor
from threading import Thread

class Chat:
    def __init__(self, chatname, port_receiving, port_sending):

        self.__name = chatname
        self.__port_receiving = port_receiving
        self.__port_sending = port_sending
        self.init_queues(port_receiving, port_sending)
        self.init_monitor()

    def get_ports(self):
        return self.__port_receiving, self.__port_sending

    def get_counter_users(self):
        return self.__monitor.get_counter_users() 

    def init_queues(self, port_receiving, port_sending):
        self.__receive_context = zmq.Context()
        self.__receiving_mq = self.__receive_context.socket(zmq.SUB)
        self.__receiving_mq.bind(f"tcp://*:{port_receiving}")
        self.__receiving_mq.setsockopt_string(zmq.SUBSCRIBE, "")

        self.__sending_context = zmq.Context()
        self.__sending_mq = self.__sending_context.socket(zmq.PUB)
        self.__sending_mq.bind(f"tcp://*:{port_sending}")

        self.__messages_thread = Thread(target=self.waiting_message)

    def init_monitor(self):
        self.__monitor = ChatMonitor(self.__name, self.__receiving_mq.get_monitor_socket())
        self.__monitor_thread = Thread(target=self.__monitor.start_monitoring)

    def start(self):
        self.__monitor_thread.start()
        self.__messages_thread.start()
        print(f"{self.__name}\t|\tStarted")

        self.__messages_thread.join()
        self.__monitor_thread.join()
        self.__sending_mq.close()
        self.__receiving_mq.close()

    def waiting_message(self):
        while True:
            message = self.__receiving_mq.recv_json()

            name_user, text_received = message["user"], message["message"]

            print(f"{self.__name}\t|\tReceived from {name_user}: {text_received}")

            self.__sending_mq.send_json(message)
