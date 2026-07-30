import customtkinter as ctk
from CTkMenuBar import *
import platform
import tkinter.messagebox

from gui.windows import Windows
from gui.macos import macOS
from gui.linux import Linux
from core.config import OpenSettings

app = ctk.CTk()
app.title("betterPowerSchedule")
app.geometry("439x371")

def openconfig():
    OpenSettings(app)

menu = CTkMenuBar(master=app)
button = menu.add_cascade("Menu")
dropdown = CustomDropdownMenu(widget=button)
dropdown.add_option(option="Open Setting")
dropdown.add_separator() 
dropdown.add_option(option="About") 

if platform.system() == "Windows":
    Windows(app).place(relx=0.5, rely=0.5, anchor="center")
elif platform.system() == "Darwin":
    macOS(app).place(relx=0.5, rely=0.5, anchor="center")
elif platform.system() == "Linux":
    Linux(app).place(relx=0.5, rely=0.5, anchor="center")
else:
    tkinter.messagebox.showerror("OS Error", "bPS can't support with this operating system.\nbPS supports only Windows (10+), macOS (with Apple Silicon) and Linux; not this OS.")

app.mainloop()