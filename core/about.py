import customtkinter as ctk

class OpenAbout(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.title("About")
        self.geometry("300x200")
        self.attributes("-topmost", True)

        label = ctk.CTkLabel(self, text="About - Coming soon")
        label.pack(expand=True, fill="both")