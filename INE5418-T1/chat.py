import zmq

class Chat:
    def __init__(self):
        self.__receive_context = zmq.Context()
        self.__receiving_mq = self.__receive_context.socket(zmq.REP)
        self.__receiving_mq.bind("tcp://*:5556")

        self.__sending_context = zmq.Context()
        self.__sending_mq = self.__sending_context.socket(zmq.PUB)
        self.__sending_mq.bind("tcp://*:5557")

    def waiting_message(self):
        while True:
            message = self.__receiving_mq.recv_json()

            name_user, text_received = message["user"], message["message"]

            print(f"Received {name_user} {text_received}")

            self.__receiving_mq.send_string("Received")

            self.__sending_mq.send_json(message)
    
chat = Chat()
chat.waiting_message()