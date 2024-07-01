import tkinter as tk
from tkinter import W, filedialog as fd
from tkinter import ttk
from passwordbruteforce.password_solver import PasswordSolver
import threading

class ConsumerApp(tk.Tk):
    def selecionar_arquivo(self):
        filedialogue = fd.askopenfilename(title="Selecione o arquivo")
        return filedialogue

    def _init_passwdsolver(self):
        self.passwd_solver = PasswordSolver(self.endereco_entry.get())
        self.solve_label = tk.Label(text="Aguardando senha...")
        self.solve_label.grid(row=2, columnspan=2, sticky="nsew")
        self.wait_solve = threading.Thread(target=self.passwd_solver.wait_password, args=(self._change_solve_label,))
        self.wait_solve.start()

    def _change_solve_label(self, _text):
        self.solve_label.config(text=_text)

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Consumer")
        self.endereco_label = tk.Label(master, text="Endereço IP:")
        self.endereco_entry = tk.Entry(master)
        self.endereco_label.grid(row=0, column=0, sticky=W, pady=1)
        self.endereco_entry.grid(row=0, column=1, sticky=W, pady=1)

        # Enviar
        self.send_btn = tk.Button(master, text="Enviar", command=self._init_passwdsolver)
        self.send_btn.grid(row=1, columnspan=2, sticky="nsew", pady=1)
