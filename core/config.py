import customtkinter as ctk
import tkinter.messagebox
import json
import os

class OpenSettings(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.path_to_config_file = os.path.join(os.path.dirname(__file__), "..", "assets", "settings.json")

        with open(self.path_to_config_file, "r", encoding="utf-8") as fileconfig:
            self.fileconfignow = json.load(fileconfig)

        self.title("Settings")
        self.attributes("-topmost", True)

        self.configframe = ctk.CTkFrame(self)
        self.configframe.pack(expand=True, fill="both")

        ctk.CTkLabel(self.configframe , text="Appearance").grid(row=0, column=0)
        self.appearance = ctk.CTkOptionMenu(self.configframe , values=["system", "light", "dark"])
        self.appearance.grid(row=0, column=1)
        self.appearance.set(f"{self.fileconfignow["appearance"]}")

        ctk.CTkLabel(self.configframe , text="Theme").grid(row=1, column=0)
        self.theme = ctk.CTkOptionMenu(self.configframe, values=["blue", "green", "dark-blue"])
        self.theme.grid(row=1, column=1)
        self.theme.set(f"{self.fileconfignow["color"]}")

        ctk.CTkButton(self.configframe ,text="Apply", command=self.savechange).grid(row=2, column=1)

    def savechange(self):
        self.changes = {
            "appearance":self.appearance.get(),
            "color":self.theme.get()
        }
        with open(self.path_to_config_file, "w", encoding="utf-8") as fileconfig:
            json.dump(self.changes, fileconfig, ensure_ascii=False, indent=2)
        tkinter.messagebox.showinfo("Saved change!", "Restart bPS to apply!")