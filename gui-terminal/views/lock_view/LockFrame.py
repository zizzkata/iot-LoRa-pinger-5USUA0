from tkinter import *
from config import *
from views.lock_views.LockKeypad import *

center_label_text: str = "Enter code to unlock"
center_label_fg: str = "white"
center_label_bg: str = "black"

class LockFrame(Frame):
    def keypad_number_handler(self, number: int):
        # self.password_entry.append(number)
        pass

    def keypad_accept_handler(self):
        pass

    def keypad_delete_handler(self):
        pass


    def __init__(self, window) -> None:
        super().__init__(window)
        self.password_entry = []
        self.pack()
        self.configure(bg="black")
        self.center_label = Label(
            self,
            font=header_font,
            bg=center_label_bg,
            fg=center_label_fg,
        )
        self.password_entry = Entry(self, show="*", font=header_font, bg="black", fg="white", justify="center", width=23)
        # self.center_label.pack()
        self.center_label.pack(pady=20)
        # self.password_entry.pack()
        self.password_entry.pack(pady=10)
        self.keypad_frame = LockKeypad(
            self,
            self.keypad_number_handler,
            self.keypad_accept_handler,
            self.keypad_delete_handler
        )
        self.pack()
        