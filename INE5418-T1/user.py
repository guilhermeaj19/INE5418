# from multiprocessing import Process
from threading import Thread
import zmq

class User:
    def __init__(self, username):
        self.__username = username

        context = zmq.Context()
        self.__sending_mq = context.socket(zmq.REQ)
        self.__sending_mq.connect("tcp://localhost:5556")

        context = zmq.Context()
        self.__receiving_mq = context.socket(zmq.SUB)
        self.__receiving_mq.connect("tcp://localhost:5557")
        self.__receiving_mq.setsockopt_string( zmq.SUBSCRIBE, "")

        self.__receiving_thread = Thread(target=self.waiting_message)

    def start(self):
        self.__receiving_thread.start()
        self.writing_message()
        self.__receiving_thread.join()
        print("Conversa finalizada")

    def writing_message(self):
        while True:
            message_to_send = input("Digite uma mensagem: ")

            data = {"user": self.__username, "message": message_to_send}

            self.__sending_mq.send_json(data)
            print(self.__sending_mq.recv_string())

    def waiting_message(self):
        while True:
            message = self.__receiving_mq.recv_json()
            print(message)
            name_user, text_received = message["user"], message["message"]
            print(f"{name_user}: {text_received}")


username = input("Insira seu nome: ")
user = User(username)
user.start()

