# from multiprocessing import Process
from threading import Thread
import zmq
import random
import tkinter as tk
from passwordbruteforce.gui.page import Page


class ChatPage(Page):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, controller, *args, **kwargs)
        self.controller = controller
        self.init_window()

    def init_window(self):
        self.__messages = tk.Text(self)
        self.__messages.config(state="disabled")
        self.__messages.pack(fill=tk.X)

        self.__input_user = tk.StringVar()
        self.__input_field = tk.Entry(self, text=self.__input_user)
        self.__input_field.pack(side = tk.BOTTOM, fill="both")

        frame = tk.Frame(self)
        self.__input_field.bind("<Return>", self.enter_pressed)
        frame.pack()

    def enter_pressed(self,event):
        input_get = self.__input_field.get()
    
        self.writing_message(input_get)
        self.__input_user.set('')

        return "break"

    def waiting_message(self):
        while True:
            message = self.__from_server_mq.recv_json()

            name_user, text_received = message["user"], message["message"]

            self.__messages.config(state="normal")

            self.__messages.insert(tk.INSERT, '%s\n' % f"{name_user}: {text_received}")
            self.__messages.see("end")
            self.__messages.config(state="disabled")

    def show(self, username, address, *args, **kwargs):
        self.controller.geometry("806x488")
        self.tkraise()
