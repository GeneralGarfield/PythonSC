# Elf Sender for PS5/PS4
# Created By Ricardo M
# Date: 6 / 17 / 2026
# This application is as Is im not responsible for any damage caused from sending malicious elf files or corruption.
# Sends .elf files after a successful jailbreak. IP address goes in the Text Entry under IP Address, Port goes in port,
# Select the .elf file and click send. This only works on Windows Devices. Linux has not been tested... and Apple too. 

import tkinter as tk
import os
import subprocess as ss
from tkinter import Menu, filedialog, messagebox

# Gets the File Name and & Address. 
# NOTE: if the file is corrupted it should Interfere and stop the send, but if the file gets sent
# It may cause the appplication To crash. But if all else fails the PS5/PS4 will crash or a notification
# Will pop up saying Error.
def file_Button():
    # Open the file dialog and return the selected file path
    try:
        file = filedialog.askopenfile(mode="r", filetypes=[(".elf Files", "*.elf")])
        if file:
            return file.name
        return None
    except:
        tk.messagebox.showerror(title= "Error", message= "File May be Corrupted or File name is too large to read.")

    
# The window will be used to attein the port and IP address from the User.
def Main_window():
    #Window Size and Title (Add Title Image Later)
    Window = tk.Tk()

    Window.geometry("300x200")

    Window.resizable(height=False, width=False)

    Window.title("File Sender To PS5")

# --------------------------------------------------------------------------
    #Declares the String
    IP_var=tk.StringVar()
    port_var=tk.StringVar()
    file_var = tk.StringVar()

    #Command That Sends It
    def Command_Line_Send():
        IP_address = IP_var.get()
        Port_address = port_var.get()
        file_address = file_var.get()

        command = (f"payload_sender.py {IP_address} {Port_address} {file_address}")
    
        ss.run(command)
# --------------------------------------------------------------------------

    #Labels to Help the User, Includes: "IP Address", "Port", and maybe "Select File"
    IP_Address_Label = tk.Label(text="PS5/PS4 IP Address")
    Port_Address_Label = tk.Label(text="Port")
    
    # Text Entry from the User IP Address / Port Address
    IP_Address = tk.Entry(textvariable= IP_var)
    Port_Address = tk.Entry(textvariable= port_var)
    
    # File Button Gets the Address of the File
    File_to_select_button = tk.Button(text="Select .Elf File", command=file_Button)
    Send_File_button = tk.Button(text="Send", command=Command_Line_Send, textvariable=file_var)

    #Place the Labels
    IP_Address_Label.place(x=20, y=20)
    Port_Address_Label.place(x=200, y=20)
    
    #Spots of the Buttons
    File_to_select_button.place(x=20, y=110)
    Send_File_button.place(x=40, y=160)

    # Places the Entries
    IP_Address.place(x=10, y = 40)
    Port_Address.place(x=150, y= 40)
    Window.mainloop()


Main_window()  
