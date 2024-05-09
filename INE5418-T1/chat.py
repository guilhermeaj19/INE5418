import zmq

class Chat:
    def __init__(self, port_receiving, port_sending):
        self.__receive_context = zmq.Context()
        self.__receiving_mq = self.__receive_context.socket(zmq.SUB)
        self.__receiving_mq.bind(f"tcp://*:{port_receiving}")
        self.__receiving_mq.setsockopt_string( zmq.SUBSCRIBE, "")

        self.__sending_context = zmq.Context()
        self.__sending_mq = self.__sending_context.socket(zmq.PUB)
        self.__sending_mq.bind(f"tcp://*:{port_sending}")

    def waiting_message(self):
        while True:
            message = self.__receiving_mq.recv_json()

            name_user, text_received = message["user"], message["message"]

            print(f"Received {name_user} {text_received}")

            self.__sending_mq.send_json(message)
