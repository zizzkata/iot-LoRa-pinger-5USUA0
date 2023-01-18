from tkinter import *
from config import *
from views.lock_view.LockKeypad import *
from views.home_view.HomeFrame import *
import controllers.lock_controller as lc

center_label_text: str = "Enter code to unlock"
center_label_fg: str = "white"
center_label_bg: str = "black"

class LockFrame(Frame):

    def get_input(self):
        return self.password_entry.get()

    def keypad_number_handler(self, number: int):
        self.password_entry.insert(END, number)	

    def keypad_accept_handler(self):
        lc.unlock_screen(self.get_input(), self.unlock_screen_callback)

    def unlock_screen_callback(self, success):
        if success:
            self.pack_forget()
            self.destroy()
            self.window.set_frame(HomeFrame(self.window))
        else:
            print("Incorrect password")
            self.password_entry.delete(0, END)
            self.center_label.config(text="Incorrect code")
            self.center_label.after(3000, lambda:self.center_label.config(text="Enter code", fg="red"))


        # self.password_entry.delete(0, END)
        
    
    def keypad_delete_handler(self):
        self.password_entry.delete(0, END)

    def __init__(self, window) -> None:
        super().__init__(window)
        self.window = window
        # self.pack()
        self.configure(bg="black")
        self.center_label = Label(
            self,
            text=center_label_text,
            font=header_font,
            bg=center_label_bg,
            fg=center_label_fg,
            text=center_label_text
        )
        self.password_entry = Entry(self, show="*", font=header_font, bg="black", fg="white", justify="center", width=23)
        self.center_label.grid(row=0, column=0, pady=40)
        self.password_entry.grid(row=1, column=0, pady=20)
        self.keypad_frame = LockKeypad(
            self,
            self.keypad_number_handler,
            self.keypad_accept_handler,
            self.keypad_delete_handler
        )
        self.pack()
        