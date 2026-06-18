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
        file = filedialog.askopenfile(mode="r", filetypes=[(".elf/.js Files", "*.elf *.js")])
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
    #Test 1
    #THIS SHOULD BE THE LOCATION OF THE FILE
    def file_path_and_the_sender(): #I Guess IM OUT OF IDEAS, BUT IT SHOULD WORK! IT DID!!
        file_path = file_Button()
    #   Command that Sends the Selected File
        def Command_Line_Send():
            IP_address = IP_var.get()
            Port_address = port_var.get()
            a = file_path
            command = (f"python.exe payload_sender.py {IP_address} {Port_address} {a}")
            ss.run(command)

        #Spawns In the Send File and it stays there for the Duration of the Program.
        Send_File_button = tk.Button(text="Send", command=Command_Line_Send)
        Send_File_button.place(x=125, y=160)

        #Displays the name of the file
        File_name = tk.Label(text=f"{file_path}")
        File_name.place(x=80, y=85)

    #Labels to Help the User, Includes: "IP Address", "Port", and maybe "Select File"
    IP_Address_Label = tk.Label(text="PS5/PS4 IP Address")
    Port_Address_Label = tk.Label(text="Port")
    # Text Entry from the User IP Address / Port Address
    IP_Address = tk.Entry(textvariable= IP_var)
    Port_Address = tk.Entry(textvariable= port_var)
    # File Button Gets the Address of the File
    File_to_select_button = tk.Button(text="Select .elf or .js File", command=file_path_and_the_sender)
    #Place the Labels
    IP_Address_Label.place(x=20, y=20)
    Port_Address_Label.place(x=200, y=20)
    #This just says Name of File, the address of the file shows up later.

    Name_OF = tk.Label(text="File Name: ")

    #Spots of the Buttons

    File_to_select_button.place(x=20, y=110)

    # Places the Entries
    IP_Address.place(x=10, y = 40)
    Port_Address.place(x=150, y= 40)
    # Places the Name_OF
    Name_OF.place(x=20, y = 85)
    Window.mainloop()
Main_window()  
