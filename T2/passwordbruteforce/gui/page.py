import tkinter as tk

#Classe abstrata
class Page(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, *kwargs)
        self.grid(row=0, column=0, sticky="nsew")

    def show(self, *args, **kwargs):
        pass