import subprocess as sb
import tkinter.messagebox
import customtkinter as ctk

def stop():
    execute = sb.Popen("sudo killall shutdown",
        stdin=sb.PIPE, 
        stdout=sb.PIPE, 
        stderr=sb.PIPE,
        text=True)
    stdout, stderr = execute.communicate(input=f"{ctk.CTkInputDialog(text="Because you're using macOS, you need to enter your password to continue. We promise not to send your password to us!", title="Enter password").get_input()}\n")
    if execute.returncode != 0:
        tkinter.messagebox.showerror("Error", f"{stderr}")
    else:
        tkinter.messagebox.showinfo("Cancelled", "Schedule successfully cancelled")

def start(time, action, comment):
    if comment == '':
        if action =='Shut down':
            execute = sb.Popen(['sudo', 'shutdown', '-h', '+'+str(time)],
                    stdin=sb.PIPE, 
                    stdout=sb.PIPE, 
                    stderr=sb.PIPE,
                    text=True)
        else:
            execute = sb.Popen(['sudo', 'shutdown', '-r', '+'+str(time)],
                    stdin=sb.PIPE, 
                    stdout=sb.PIPE, 
                    stderr=sb.PIPE,
                    text=True)
    else:
        if action =='Shut down':
            execute = sb.Popen(['sudo', 'shutdown', '-h', '+'+str(time), comment]
                    stdin=sb.PIPE, 
                    stdout=sb.PIPE, 
                    stderr=sb.PIPE,
                    text=True,)
        else:
            execute = sb.Popen(['sudo', 'shutdown', '-r', '+'+str(time), comment]
                    stdin=sb.PIPE, 
                    stdout=sb.PIPE, 
                    stderr=sb.PIPE,
                    text=True)

    stdout, stderr = execute.communicate(input=f"{ctk.CTkInputDialog(text="Because you're using macOS, you need to enter your password to continue. We promise not to send your password to us!", title="Enter password").get_input()}\n")
    if execute.returncode != 0:
        tkinter.messagebox.showerror("Error", f"{stderr}")
    else:
        tkinter.messagebox.showinfo("Started", "Schedule successfully started")