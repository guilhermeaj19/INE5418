import tkinter as tk
from tkinter import W, filedialog as fd
from tkinter import ttk


class App(tk.Frame):
    def selecionar_arquivo(self):
        filedialogue = fd.askopenfilename(title="Selecione o arquivo")
        return filedialogue

    def __init__(self, master=None):
        super().__init__(master)
        # self.pack()

        # Endereço
        self.endereco_label = tk.Label(master, text="Endereço IP:")
        self.endereco_entry = tk.Entry(master)
        self.endereco_label.grid(row=0, column=0, sticky=W, pady=2)
        self.endereco_entry.grid(row=0, column=1, sticky=W, pady=2)

        # Selecionar arquivo
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
            " Lista",
        )
        self.tipo_label.grid(row=3, column=0, sticky="nsew", pady=2, padx=2)
        self.tipo_dropwdown.grid(row=3, column=1, sticky="nsew", pady=2)
        self.tipo_dropwdown.current(0)

        #Configuração ataque
        #TODO alterar para casos específicos

        # Enviar
        self.send_btn = tk.Button(master, text="Enviar")
        self.send_btn.grid(row=4, columnspan=2, sticky="nsew", pady=2, padx=2)



myapp = App()
myapp.mainloop()
