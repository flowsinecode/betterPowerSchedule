import customtkinter as ctk
import CTkMenuBar
import platform
import tkinter.messagebox

from gui.windows import Windows
from gui.macos import macOS
from gui.linux import Linux

app = ctk.CTk()
app.title("betterPowerSchedule")

menu = CTkMenuBar(master=app)
button = menu.add_cascade("Setting")

if platform.system() == "Windows":
    Windows(app)
elif platform.system() == "Darwin":
    macOS(app)
elif platform.system() == "Linux":
    Linux(app)
else:
    tkinter.messagebox.showerror("bPS can't support with this operating system", "bPS supports only Windows (10+), macOS (with Apple Silicon) and Linux; not this OS")

app.mainloop()