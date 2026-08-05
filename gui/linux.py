import customtkinter as ctk
from CTkSpinbox import *

from core.run import linux

class Linux(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.timepicker = ctk.CTkFrame(self)
        self.timepicker.grid(row=0, column=0)

        ctk.CTkLabel(self.timepicker, text="Time                 ").grid(row=0, column=0)

        self.hours = ctk.IntVar()
        self.hours_pick = CTkSpinbox(self.timepicker,
            start_value = 0,
            min_value = 0,
            max_value = 24,
            scroll_value = 2,
            variable = self.hours)
        self.hours_pick.grid(row=1, column=0)
        ctk.CTkLabel(self.timepicker, text="h").grid(row=2, column=0)

        self.mins = ctk.IntVar()
        self.mins_pick = CTkSpinbox(self.timepicker,
            start_value = 0,
            min_value = 0,
            max_value = 60,
            scroll_value = 2,
            variable = self.mins)
        self.mins_pick.grid(row=1, column=1)
        ctk.CTkLabel(self.timepicker, text="m").grid(row=2, column=1)

        self.secs = ctk.IntVar()
        self.secs_pick = CTkSpinbox(self.timepicker,
            start_value = 0,
            min_value = 0,
            max_value = 60,
            scroll_value = 2,
            variable = self.mins)
        self.secs_pick.grid(row=1, column=2)
        ctk.CTkLabel(self.timepicker, text="s").grid(row=2, column=2)

        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.grid(row=1, column=0)

        ctk.CTkLabel(self.action_frame, text="  Action                                    ").grid(row=0, column=0)
        self.action = ctk.StringVar(value="Shut down")
        self.action_option = ctk.CTkOptionMenu(self.action_frame, values=["Shut down", "Restart"], variable=self.action)
        self.action_option.grid(row=0, column=1)

        ctk.CTkLabel(self.action_frame, text="  Comment                               ").grid(row=1, column=0)
        self.comment = ctk.CTkEntry(self.action_frame, placeholder_text="Make it blank to disable")
        self.comment.grid(row=1, column=1)

        self.buttons = ctk.CTkFrame(self)
        self.buttons.grid(row=2, column=0)

        self.stop = ctk.CTkButton(self.buttons, text="Stop", fg_color="#D32F2F", hover_color="#9A0007", command=linux.stop)
        self.stop.grid(row=0, column=0)

        ctk.CTkLabel(self.buttons, text="      ").grid(row=0, column=1)

        self.start = ctk.CTkButton(self.buttons, text="Start", command=self.start)
        self.start.grid(row=0, column=2)

    def start(self):
        self.timetostart = (self.hours_pick.get() * 60) + self.mins_pick.get() + (round(self.secs_pick.get() / 60)) # Low accuracy
        linux.start(self.timetostart, self.action_option.get(), self.comment.get())