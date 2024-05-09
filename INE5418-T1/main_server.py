from chat import Chat
from threading import Thread

class MainServer:
    def __init__(self):
        self.__chats = [Chat(5556,5557),
                        Chat(5558,5559),
                        Chat(5560,5561)
        ]

        self.__chats_threads = []
        for chat in self.__chats:
            self.__chats_threads.append(Thread(target=chat.waiting_message))

    def start(self):
        for chat in self.__chats_threads:
            chat.start()
        for chat in self.__chats_threads:
            chat.join()

mainserver = MainServer()
mainserver.start()