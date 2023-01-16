from tkinter import *
from tkinter import ttk
from config import *

border_radius: int = 10
num_pad_numbers: list = range(10)
button_style: str = "Rounded.TButton"
button_padx: int = 5
button_pady: int = 5
keypad_button_bg: str = "grey30"
keypad_button_fg: str = "white"
keypad_button_active_background : str = "green"
keypad_button_relief: str = "sunken"
keypad_button_width: int = 6
keypad_button_height: int = 2

accept_button_bg: str = "green"
accept_button_fg: str = "black"
delete_button_bg: str = "red"
delete_button_fg: str = "black"


class LockKeypad(Frame):
    def create_buttons(self):
        button_list: list = []
        for index, value in enumerate(reversed(num_pad_numbers)):
            row_index: int = index // 3
            column_index: int = index % 3
            if index == len(num_pad_numbers) - 1:
                column_index = 1 # define center
            button_list.append(
                self.create_button(
                    str(value),
                    row_index, 
                    column_index,
                    keypad_button_bg,
                    keypad_button_fg,
                    keypad_button_active_background,
                    keypad_button_relief,
                    keypad_button_width,
                    keypad_button_height,
                    lambda x = value: self.insert_number_handler(x)
                    )
            )
        accept_button = self.create_button(
            "Accept",
            4,  # row
            0,  # column
            accept_button_bg,
            accept_button_fg,
            keypad_button_active_background,
            keypad_button_relief,
            keypad_button_width,
            keypad_button_height,
            self.accept_handler
        )
        button_list.append(accept_button)
        delete_button = self.create_button(
            "Delete",
            4,  # row
            2,  # column
            delete_button_bg,
            delete_button_fg,
            keypad_button_active_background,
            keypad_button_relief,
            keypad_button_width,
            keypad_button_height,
            self.delete_handler
        )
        button_list.append(delete_button)
        return button_list

    def create_button(self,
        text: str,
        row: int,
        col: int,
        bg: str,
        fg: str,
        activebackground: str,
        relief: str,
        width: int,
        height: int,
        command: callable
    ):
        button = Button(self,
            text=text,
            bg=bg,
            fg=fg,
            activebackground=activebackground,
            relief=relief,
            width=width,
            height=height,
            command=command)
        button.grid(row=row, column=col, padx=button_padx, pady=button_pady)
        return button

    def __init__(self,
        window,
        insert_number_handler,
        accept_handler,
        delete_handler
    ) -> None:
        super().__init__(window)
        self.keypad_numbers_object: list = []
        self.insert_number_handler = insert_number_handler
        self.accept_handler = accept_handler
        self.delete_handler = delete_handler
        # self.pack()
        # self.configure(bg="black")
        self.style = ttk.Style()
        self.style.configure(
            "Rounded.TButton", relief="sunken", borderradius=border_radius)
        self.keypad_numbers_object.append(
            self.create_buttons())
        self.grid(row=4, column=0, pady=10)
