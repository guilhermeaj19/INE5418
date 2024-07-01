import tkinter as tk
import threading
from passwordbruteforce.archiver import Archiver

class ArchiverApp(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Archiver")
        self.init_window()
        self.archiver = Archiver()
        self.wait_result = threading.Thread(target=self.archiver.wait_result, args=(self._update_log,))
        self.wait_result.start()

    def init_window(self):
        self.__messages = tk.Text(self)
        self.__messages.config(state="disabled")
        self.__messages.pack(fill=tk.X)

        # self.__input_user = tk.StringVar()
        # self.__input_field = tk.Entry(self, text=self.__input_user)
        # self.__input_field.pack(side = tk.BOTTOM, fill="both")

        frame = tk.Frame(self)
        # self.__input_field.bind("<Return>", self.enter_pressed)
        frame.pack()

    def enter_pressed(self,event):
        input_get = self.__input_field.get()
    
        self.writing_message(input_get)
        self.__input_user.set('')

        return "break"

    def _update_log(self, text):
        self.__messages.config(state="normal")

        self.__messages.insert(tk.INSERT, '%s\n' % f"{text}")
        self.__messages.see("end")
        self.__messages.config(state="disabled")
