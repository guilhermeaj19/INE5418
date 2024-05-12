from server.chat import Chat
from threading import Thread
import zmq

class MainServer:
    def __init__(self):
        self.__chats = []

        self.__find_chat_context = zmq.Context()
        self.__find_chat_mq = self.__find_chat_context.socket(zmq.REP)
        self.__find_chat_mq.bind(f"tcp://*:5555")
        self.__finder_thread = Thread(target=self.waiting_conection)

    def create_new_chat(self) -> Chat:
        self.__chats.append(Chat(f"Chat{len(self.__chats)}"))
        self.__chats[-1].start()
        return self.__chats[-1]

    def find_best_chat(self):
        best_chat_user_counter = 10
        best_chat = None

        for chat in self.__chats:
            user_counter = chat.get_counter_users()
            if user_counter == 1:
                return chat.get_ports()
            
            if user_counter < best_chat_user_counter:
                best_chat = chat
                best_chat_user_counter = user_counter

        if not best_chat:
            best_chat = self.create_new_chat()

        return best_chat.get_ports()

    def waiting_conection(self):
        while True:
            request = self.__find_chat_mq.recv_string()

            from_client_port, to_client_port = self.find_best_chat()
            
            data = {"to_server": from_client_port, "from_server": to_client_port}
            self.__find_chat_mq.send_json(data)

    def start(self):
        self.__finder_thread.start()
        self.__finder_thread.join()

        for chat in self.__chats:
            chat.join()