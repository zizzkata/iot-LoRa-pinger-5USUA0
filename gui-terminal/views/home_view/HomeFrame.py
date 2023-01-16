from tkinter import *

class HomeFrame(Frame):
    def __init__(self, window) -> None:
        super().__init__(window)
        self.pack()
        self.configure(bg="black")
        self.center_label = Label(
            self,
            font=header_font,
            bg="black",
            fg="white",
        )
        self.center_label.pack(pady=20)
        self.center_label["text"] = "Home"