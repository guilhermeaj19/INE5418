import tkinter as tk
from tkinter import W, filedialog as fd
from tkinter import ttk
from passwordbruteforce.producer import Producer
import time
import threading

class ProducerApp(tk.Tk):
    def selecionar_arquivo(self):
        self.arquivo_path = fd.askopenfilename(title="Selecione o arquivo")
        self.arquivo_text.configure(text=self.arquivo_path)

    def _init_range_frame(self):
        self.range_frame = tk.Frame()
        self.range_label = tk.Label(self.range_frame, text="Intervalo especificado")
        self.range_label.grid(row=0, columnspan=2, sticky="nsew", pady=2)
        self.first_entry = tk.Entry(self.range_frame)
        self.first_entry.insert(0, "0")
        self.first_entry.grid(row=1, column=0, sticky="nsew")
        self.second_entry = tk.Entry(self.range_frame)
        self.second_entry.insert(0, "10000000")
        self.second_entry.grid(row=1, column=1, sticky="nsew")
        # self.range_frame.grid(row=4, columnspan=2, pady=8, sticky="nsew")

    def _dropdown_callback(self, var, index, mode):
        if self.n.get() == "Intervalo":
            self.range_frame.grid(row=4, columnspan=2, pady=8, sticky="nsew")
        else:
            self.range_frame.grid_forget()

    def _get_param(self):
        return {"Lista": "password_files/wordlist.txt", "Intervalo": self._get_range()}[self.n.get()]

    def _get_range(self):
        return f"{self.first_entry.get()}-{self.second_entry.get()}"
    
    def _init_producer(self):
        self.producer = Producer(self.endereco_entry.get())

    def _get_mode(self):
        return {"Lista": "list", "Intervalo": "range"}[self.n.get()]

    def _sucess_msg(self):
        self.sucess_label.grid(row=6, columnspan=2, sticky="nsew", pady=2, padx=2)
        time.sleep(3)
        self.sucess_label.grid_forget()

    def _send_producer(self):
        if not self.producer:
            self._init_producer()
        self.producer.solve_passwords(self.arquivo_path, self._get_mode(), self._get_param())
        self.sucess_thread = threading.Thread(target=self._sucess_msg)
        self.sucess_thread.start()

    def __init__(self, master=None):
        super().__init__(master)
        # self.pack()

        # Endereço
        self.title("Producer")
        self.producer = None
        self.endereco_label = tk.Label(master, text="Tuplespace IPs:")
        self.endereco_entry = tk.Entry(master)
        self.endereco_entry.insert(0, "127.0.0.1:5551,127.0.0.1:5552,127.0.0.1:5553")
        self.endereco_label.grid(row=0, column=0, sticky=W, pady=2)
        self.endereco_entry.grid(row=0, column=1, sticky=W, pady=2)

        # Selecionar arquivo
        self.arquivo_path = None
        self.arquivo_text = tk.Label(master, text="Nenhum arquivo selecionado...")
        self.arquivo_btn = tk.Button(
            master, text="Selecionar arquivo", command=self.selecionar_arquivo
        )
        self.arquivo_text.grid(row=1, columnspan=2, sticky="nsew", pady=5)
        self.arquivo_btn.grid(row=2, columnspan=2, sticky="nsew", pady=2)

        # Dropdown tipos de ataque
        self.n = tk.StringVar() 
        self.tipo_label = tk.Label(master, text="Tipo de ataque:")
        self.tipo_dropwdown = ttk.Combobox(master, textvariable=self.n)
        self.tipo_dropwdown["values"] = (
            "Intervalo",
            "Lista",
        )
        self._init_range_frame()
        self.n.trace_add("write", self._dropdown_callback)
        self.tipo_label.grid(row=3, column=0, sticky="nsew", pady=2, padx=2)
        self.tipo_dropwdown.grid(row=3, column=1, sticky="nsew", pady=2)
        self.tipo_dropwdown.current(0)
        #Configuração ataque
        #TODO alterar para casos específicos

        # Enviar
        self.send_btn = tk.Button(master, text="Enviar", command=self._send_producer)
        self.send_btn.grid(row=5, columnspan=2, sticky="nsew", pady=2, padx=2)
        self.sucess_label = tk.Label(master, text="Enviado com sucesso!")
