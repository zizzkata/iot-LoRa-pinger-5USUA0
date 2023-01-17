from tkinter import *
from config import *
import controllers.trackers_controller as tc
from views.home_view.TrackerButton import TrackerButton
from views.tracker_settings_view.TrackerInfo import TrackerInfo

number_trackers_row: int = 5

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
                    lambda x = value: self.tracker_handler(x),
                    lambda x = value: self.tracker_handler_settings(x)
                )
            )

    def add_tracker(
        self,
        text: str,
        row_index: int,
        column_index: int,
        callback_click: callable,
        callback_hold: callable
    ) -> Button:
        tracker_button = TrackerButton(
            self, 
            text=text, 
            row=row_index, 
            column=column_index, 
            callback_click=callback_click,
            callback_hold=callback_hold,
        )
        return tracker_button

    def tracker_handler(self, tracker: dict):
        print(tracker)
    
    def tracker_handler_settings(self, tracker: dict):
        settings = TrackerInfo(self.window, tracker)

    def __init__(self, window) -> None:
        super().__init__(window)
        self.window = window
        self.tracker_buttons = []
        self.configure(bg="black")
        tc.load_trackers(self.add_trackers)
        self.pack()

        
    