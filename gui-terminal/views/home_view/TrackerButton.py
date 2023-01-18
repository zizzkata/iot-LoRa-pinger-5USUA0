from tkinter import *
from threading import Timer
import time

hold_time: float = .8

tracker_button_bg: str = "grey30"
tracker_button_fg: str = "white"
tracker_button_active_background : str = "green"
tracker_button_relief: str = "sunken"
tracker_button_width: int = 10
tracker_button_height: int = 2
tracker_button_pady: int = 10
tracker_button_padx: int = 10


class TrackerButton(Button):

    def _timer_callback(self):
        if time.time() - self.timePressed >= hold_time:
            self.hold_callback()

    def _set_timer(self, event):
        timer = Timer(hold_time, self._timer_callback)
        timer.start()
        self.timePressed = time.time()
    
    def _handle_release(self, event):
        if time.time() - self.timePressed < hold_time:
            self.click_callback()
        self.timePressed = time.time()

    def __init__(self, master,
        text: str,
        row: int,
        column: int,
        callback_click: callable,
        callback_hold: callable,
    ) -> None:
        super().__init__(
            master=master,
            text=text,
            bg=tracker_button_bg,
            fg=tracker_button_fg,
            activebackground=tracker_button_active_background,
            relief=tracker_button_relief,
            width=tracker_button_width,
            height=tracker_button_height,
            pady=tracker_button_pady,
            padx=tracker_button_padx,
        )
        self.timePressed = 0
        self.click_callback = callback_click
        self.hold_callback = callback_hold
        self.bind("<Button-1>", self._set_timer)
        self.bind("<ButtonRelease-1>", self._handle_release)
        self.grid(row=row, column=column)
    