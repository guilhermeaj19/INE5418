import tkinter as tk
from user.connect_page import ConnectPage
from user.chat_page import ChatPage

class ChatApp(tk.Tk):

    def __init__(
        self,
        title: str | None = None,
        width: int | None = None,
        height: int | None = None,
    ) -> None:
        super().__init__()
        self._configure_window(title, width, height)
        self._init_frames()
        self.show("ConnectPage")

    def _configure_window(self, title, width, height):
        self.title(title if title else "ChatApp")
        self.resizable(False, False)

    def _init_frames(self):
        self.__frames = {}
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        for page in [ConnectPage, ChatPage]:
            self.__frames[page.__name__] = page(self.container, self)
            self.__frames[page.__name__].grid(row=0, column=0, sticky="nsew")

    def show(self, frame_name: str, *args, **kwargs):
        self.__frames[frame_name].show(*args, **kwargs)