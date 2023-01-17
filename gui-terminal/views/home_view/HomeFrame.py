from tkinter import *
from config import *
from views.home_view.TrackersFrame import TrackersFrame

center_label_text: str = "Trackers"
center_label_fg: str = "white"
center_label_bg: str = "black"

add_tracker_button_text: str = "Add Tracker"
add_tracker_button_bg: str = "grey30"
add_tracker_button_fg: str = "white"
add_tracker_button_active_background : str = "green"
add_tracker_button_relief: str = "sunken"
add_tracker_button_width: int = 10
add_tracker_button_height: int = 2
add_tracker_button_pady: int = 10
add_tracker_button_padx: int = 10

remove_tracker_button_text: str = "Remove Tracker"


class HomeFrame(Frame):


    def handle_add_tracker_button(self):
        pass

    def handle_remove_tracker_button(self):
        pass

    def __init__(self, window) -> None:
        super().__init__(window)
        self.configure(bg="black")
        self.center_label = Label(
            self,
            font=header_font,
            bg=center_label_bg,
            fg=center_label_fg,
        )
        self.center_label.pack(pady=20)
        self.center_label["text"] = center_label_text
        self.trackers_frame = TrackersFrame(self)
        # self.trackers_frame.pack()

        self.add_tracker_button = Button(
            self,
            text=add_tracker_button_text,
            bg=add_tracker_button_bg,
            fg=add_tracker_button_fg,
            activebackground=add_tracker_button_active_background,
            relief=add_tracker_button_relief,
            width=add_tracker_button_width,
            height=add_tracker_button_height,
            command=self.handle_add_tracker_button
        )
        self.remove_tracker_button = Button(
            self,
            text=remove_tracker_button_text,
            bg=add_tracker_button_bg,
            fg=add_tracker_button_fg,
            activebackground=add_tracker_button_active_background,
            relief=add_tracker_button_relief,
            width=add_tracker_button_width,
            height=add_tracker_button_height,
            command=self.handle_remove_tracker_button
        )
        
        # self.add_tracker_button.grid(
        #     row=0,
        #     column=0,
        #     padx=add_tracker_button_padx,
        #     pady=add_tracker_button_pady
        # )
        self.add_tracker_button.pack()
        self.remove_tracker_button.pack()



        