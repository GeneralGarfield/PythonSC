# Convertion GUI Version 0.1
# Date 4/3/2025
# Author Ricardo


#Libraries
import tkinter as tk
from tkinter import Menu, filedialog, messagebox
import os
import webbrowser
from PIL import Image, ImageTk



#Functions for the Menu
def file_opener():
    test = tk.filedialog.askopenfile(mode="r", 
                                     filetypes = [("Image Files", "*.png")]
    )
    if test:
        return test.name
    return None


    

def imagetest():
    file_path = file_opener
    if file_path:
        image = Image.open(file_opener)
        image2 = ImageTk.PhotoImage(image)
        label = root.Label(image = image2)
        label.pack()


def link():
    webbrowser.open_new_tab("https://github.com/GeneralGarfield")
def saveas():
    tk.tkinter.filedialog.asksaveasfilename()









#Opens file in the same directory
directory_path = os.path.dirname(__file__)
file_path = os.path.join(directory_path, 'test.ico')

# Creates the main Window and Icon
root = tk.Tk()
root.title("Converter")
root.iconbitmap(file_path)
root.geometry("580x480")



# This starts the menu bar with the option menu. 
menubar = Menu(root)

# This is the selection for the File category
filemenu = Menu(menubar, tearoff= 0)

filemenu.add_command(label="Open File", command=file_opener)

filemenu.add_command(label="View Convertions", command="placeholder")

filemenu.add_command(label="Settings", command="placeholder")

filemenu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="File", menu=filemenu)

#Help Option
Help = Menu(menubar, tearoff=0)

Help.add_command(label="Tutorial", command="PlaceHolder")
menubar.add_cascade(label="Help", menu=Help)


#About me
About = Menu(menubar, tearoff= 0)

About.add_command(label="About Me", command=imagetest)
About.add_command(label="Github", command=link)
menubar.add_cascade(label="About", menu=About)





#These last two go last to run the menubar DONT CHANGE IT

root.config(menu=menubar)
root.mainloop()



