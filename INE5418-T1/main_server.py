from chat import Chat
from threading import Thread
from multiprocessing import *

class MainServer:
    def __init__(self):
        self.__chats = [Chat("Chat 1",5556,5557),
                        Chat("Chat 2",5558,5559),
                        Chat("Chat 3",5560,5561)
                       ]

        self.__chats_threads = []
        for chat in self.__chats:
            self.__chats_threads.append(Thread(target=chat.start))

    def start(self):
        for chat in self.__chats_threads:
            chat.start()
        for chat in self.__chats_threads:
            chat.join()

mainserver = MainServer()
mainserver.start()