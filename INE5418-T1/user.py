# from multiprocessing import Process
from threading import Thread
import zmq
import random
import tkinter as tk


class User:
    def __init__(self, username):
        self.__username = username

    def init_queues(self):
        #TODO: Fazer uma comunicação inicial com o MainServer para requisitar o chat

        possible_chats = [(5556,5557),
                          (5558,5559),
                          (5560,5561)
                          ] #Apenas para testes
        sending_port, receiving_port = random.choice(possible_chats)

        context = zmq.Context()
        self.__sending_mq = context.socket(zmq.PUB)
        self.__sending_mq.connect(f"tcp://localhost:{sending_port}")

        context = zmq.Context()
        self.__receiving_mq = context.socket(zmq.SUB)
        self.__receiving_mq.connect(f"tcp://localhost:{receiving_port}")
        self.__receiving_mq.setsockopt_string( zmq.SUBSCRIBE, "")

        self.__receiving_thread = Thread(target=self.waiting_message)

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
        self.__receiving_thread.start()
        self.__window.mainloop()

        #Desligandos sockets
        self.__receiving_mq.close()
        self.__sending_mq.close()
        exit()

    def writing_message(self, message_to_send):
        data = {"user": self.__username, "message": message_to_send}
        self.__sending_mq.send_json(data)

    def waiting_message(self):
        while True:
            message = self.__receiving_mq.recv_json()

            name_user, text_received = message["user"], message["message"]

            self.__messages.config(state="normal")

            self.__messages.insert(tk.INSERT, '%s\n' % f"{name_user}: {text_received}")
            self.__messages.see("end")
            self.__messages.config(state="disabled")

username = input("Insira seu nome: ")
user = User(username)
user.start()

