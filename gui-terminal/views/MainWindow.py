from tkinter import *
from config import *
from views.lock_views.LockFrame import LockFrame

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title = application_name
        self.configure(bg="black")
        self.geometry(application_size)
        self.frame = LockFrame(self)
        
    def set_frame(self, frame):
        self.frame = frame
        self.frame.pack()
