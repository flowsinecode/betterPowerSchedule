import customtkinter as ctk

class OpenSettings(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.title("Settings")
        self.geometry("300x200")
        self.attributes("-topmost", True)

        label = ctk.CTkLabel(self, text="Settings - Coming soon")
        label.pack(expand=True, fill="both")