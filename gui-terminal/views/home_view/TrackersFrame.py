from tkinter import *
from config import *
import controllers.trackers_controller as tc

number_trackers_row: int = 5

tracker_button_bg: str = "grey30"
tracker_button_fg: str = "white"
tracker_button_active_background : str = "green"
tracker_button_relief: str = "sunken"
tracker_button_width: int = 10
tracker_button_height: int = 2
tracker_button_pady: int = 10
tracker_button_padx: int = 10

class TrackersFrame(Frame):

    def add_trackers(self, trackers: list):
        for index, value in enumerate(trackers):
            row_index: int = index // number_trackers_row
            column_index: int = index % number_trackers_row
            self.tracker_buttons.append(
                self.add_tracker(
                    value['name'],
                    row_index,
                    column_index,
                    lambda x = value: self.tracker_handler(x)
                )
            )

    def add_tracker(
        self,
        text: str,
        row_index: int,
        column_index: int,
        callback: callable
    ) -> Button:
        tracker_button = Button(
            self,
            text=text,
            bg=tracker_button_bg,
            fg=tracker_button_fg, 
            font=header_font,
            activebackground=tracker_button_active_background, 
            relief=tracker_button_relief, 
            width=tracker_button_width, 
            height=tracker_button_height,
            command=callback
        )
        tracker_button.grid(
            row=row_index,
            column=column_index, 
            padx=tracker_button_padx, 
            pady=tracker_button_pady
        )
        return tracker_button

    def tracker_handler(self, tracker: dict):
        print(tracker)

    def __init__(self, window) -> None:
        super().__init__(window)
        self.tracker_buttons = []
        self.configure(bg="black")
        tc.load_trackers(self.add_trackers)
        self.pack()

        
    