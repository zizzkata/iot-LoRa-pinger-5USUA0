from tkinter import *

class TrackerInfo(Frame):
    def __init__(self, window, trackerInfo) -> None:
        super().__init__(window)
        self.configure(bg="black")
        self.pack()
        close_button = Button(
            self,
            text="Close",
            command=self.destroy
        )
        name_label = Label(
            self,
            text=trackerInfo['name'],
            bg="black",
            fg="white"
        )
        name_label.pack(side=TOP)
        close_button.pack(side=LEFT)