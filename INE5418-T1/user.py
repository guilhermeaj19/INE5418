# from multiprocessing import Process
from threading import Thread
import zmq
from tkinter import *





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


        self.__window = Tk()

        self.__messages = Text(self.__window)
        self.__messages.pack()

        self.__input_user = StringVar()
        self.__input_field = Entry(self.__window, text=self.__input_user)
        self.__input_field.pack(side=BOTTOM, fill=X)

        frame = Frame(self.__window)
        self.__input_field.bind("<Return>", self.enter_pressed)
        frame.pack()

    def enter_pressed(self,event):
        input_get = self.__input_field.get()
    
        self.writing_message(input_get)
        self.__input_user.set('')

        return "break"

    def start(self):
        self.__receiving_thread.start()
        self.__window.mainloop()
        exit()

    def writing_message(self, message_to_send):

        data = {"user": self.__username, "message": message_to_send}

        self.__sending_mq.send_json(data)
        print(self.__sending_mq.recv_string())

    def waiting_message(self):
        while True:
            message = self.__receiving_mq.recv_json()

            name_user, text_received = message["user"], message["message"]
            self.__messages.insert(INSERT, '%s\n' % f"{name_user}: {text_received}")



username = input("Insira seu nome: ")
user = User(username)
user.start()

