import subprocess as sb
import tkinter.messagebox

def stop():
    execute = sb.run("shutdown /a", capture_output=True, text=True)
    if execute.stderr:
        tkinter.messagebox.showerror("Error", f"{execute.stderr}")
    else:
        tkinter.messagebox.showinfo("Cancelled", "Schedule successfully cancelled")

def start(time, action, comment):
    if comment == '':
        if action =='Shut down':
            execute = sb.run(['shutdown', '/s', '/t', str(time)], capture_output=True, text=True)
        else:
            execute = sb.run(['shutdown', '/r', '/t', str(time)], capture_output=True, text=True)
    else:
        if action =='Shut down':
            execute = sb.run(['shutdown', '/s', '/t', str(time), '/c', comment], capture_output=True, text=True)
        else:
            execute = sb.run(['shutdown', '/r', '/t', str(time), '/c', comment], capture_output=True, text=True)

    if execute.stderr:
        tkinter.messagebox.showerror("Error", f"{execute.stderr}")
    else:
        tkinter.messagebox.showinfo("Started", "Schedule successfully started")