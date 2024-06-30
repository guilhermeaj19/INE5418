# from multiprocessing import Process
import tkinter as tk
from passwordbruteforce.gui.page import Page


class ConnectPage(Page):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, controller, *args, **kwargs)
        self.controller = controller
        self._init_name_box()
        self._init_address_box()
        self._init_btn(controller)

    def _init_name_box(self):
        self.name_label = tk.Label(self, text="Usuário:")
        self.name_label.grid(row=0, column=0, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

    def _init_address_box(self):
        self.address_label = tk.Label(self, text="Endereço IP:")
        self.address_label.grid(row=1, column=0,pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=1, column=1)

    def _init_btn(self, controller):
        self.btn = tk.Button(self, text="Entrar", command=lambda: controller.show("ChatPage",self.name_entry.get(),self.address_entry.get()))
        self.btn.grid(sticky="NSEW")

    def show(self):
        self.controller.geometry("320x99")
        self.tkraise()
