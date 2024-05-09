from chat import Chat
from threading import Thread
import random
import zmq
from multiprocessing import *

class MainServer:
    def __init__(self):
        self.__chats = [Chat("Chat 1",5556,5557),
                        Chat("Chat 2",5558,5559),
                        Chat("Chat 3",5560,5561)
                       ]

        self.__find_chat_context = zmq.Context()
        self.__find_chat_mq = self.__find_chat_context.socket(zmq.REP)
        self.__find_chat_mq.bind(f"tcp://*:5555")
        self.__finder_thread = Thread(target=self.waiting_conection)

        self.__chats_threads = []
        for chat in self.__chats:
            self.__chats_threads.append(Thread(target=chat.start))

    def waiting_conection(self):
        while True:
            request = self.__find_chat_mq.recv_string()

            for chat in self.__chats:
                print(chat.get_counter_users())
                print(chat.get_ports())

            from_client_port, to_client_port = random.choice(self.__chats).get_ports()

            data = {"to_server": from_client_port, "from_server": to_client_port}
            self.__find_chat_mq.send_json(data)

    def start(self):
        for chat in self.__chats_threads:
            chat.start()

        self.__finder_thread.start()

        for chat in self.__chats_threads:
            chat.join()
            print("A")
        
        self.__finder_thread.join()

mainserver = MainServer()
mainserver.start()