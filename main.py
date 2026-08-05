import customtkinter as ctk
from CTkMenuBar import *
import platform
import tkinter.messagebox
import sys

from gui.windows import Windows
from gui.macos import macOS
from gui.linux import Linux
from core.config import OpenSettings

app = ctk.CTk()
app.title("betterPowerSchedule")
app.resizable(False, False)

def openconfig():
    OpenSettings(app)

menu = CTkMenuBar(master=app)
button = menu.add_cascade("Menu")
dropdown = CustomDropdownMenu(widget=button)
dropdown.add_option(option="Open Setting", command=openconfig)
dropdown.add_separator() 
dropdown.add_option(option="About") 

if platform.system() == "Windows":
    Windows(app).pack(expand=True, fill="both")
elif platform.system() == "Darwin":
    macOS(app).pack(expand=True, fill="both")
elif platform.system() == "Linux":
    Linux(app).pack(expand=True, fill="both")
else:
    tkinter.messagebox.showerror("OS Error", "bPS can't support with this operating system.\nbPS supports only Windows (10+), macOS (with Apple Silicon) and Linux; not this OS.")
    app.destroy()
    sys.exit(1)

app.mainloop()