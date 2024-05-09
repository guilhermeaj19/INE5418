# from multiprocessing import Process
from threading import Thread
import zmq
import random
import tkinter as tk


class User:
    def __init__(self, username):
        self.__username = username

    def find_chat(self):
        context = zmq.Context()
        temp_mq = context.socket(zmq.REQ)
        temp_mq.connect(f"tcp://localhost:5555")

        temp_mq.send_string("FindChat")
        ports = temp_mq.recv_json()
        temp_mq.disconnect(f"tcp://localhost:5555")

        return ports["to_server"], ports["from_server"]

    def init_queues(self):

        to_server_port, from_server_port = self.find_chat()

        context = zmq.Context()
        self.__to_server_mq = context.socket(zmq.PUB)
        self.__to_server_mq.connect(f"tcp://localhost:{to_server_port}")

        context = zmq.Context()
        self.__from_server_mq = context.socket(zmq.SUB)
        self.__from_server_mq.connect(f"tcp://localhost:{from_server_port}")
        self.__from_server_mq.setsockopt_string( zmq.SUBSCRIBE, "")

        self.__from_server_thread = Thread(target=self.waiting_message)

    def init_window(self):
        self.__window = tk.Tk()

        self.__messages = tk.Text(self.__window)
        self.__messages.config(state="disabled")
        self.__messages.pack(fill=tk.X)

        self.__input_user = tk.StringVar()
        self.__input_field = tk.Entry(self.__window, text=self.__input_user)
        self.__input_field.pack(side = tk.BOTTOM, fill="both")

        frame = tk.Frame(self.__window)
        self.__input_field.bind("<Return>", self.enter_pressed)
        frame.pack()

    def enter_pressed(self,event):
        input_get = self.__input_field.get()
    
        self.writing_message(input_get)
        self.__input_user.set('')

        return "break"

    def start(self):
        self.init_window()
        self.init_queues()
        self.__from_server_thread.start()
        self.__window.mainloop()

        #Desligandos sockets
        self.__from_server_mq.close()
        self.__to_server_mq.close()
        exit()

    def writing_message(self, message_to_send):
        data = {"user": self.__username, "message": message_to_send}
        self.__to_server_mq.send_json(data)

    def waiting_message(self):
        while True:
            message = self.__from_server_mq.recv_json()

            name_user, text_received = message["user"], message["message"]

            self.__messages.config(state="normal")

            self.__messages.insert(tk.INSERT, '%s\n' % f"{name_user}: {text_received}")
            self.__messages.see("end")
            self.__messages.config(state="disabled")

username = input("Insira seu nome: ")
user = User(username)
user.start()

