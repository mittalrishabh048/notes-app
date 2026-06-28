# Notes App

## Importing Tkinter for creating Graphical User Interface(GUI) apps
import tkinter as tk
from tkinter import filedialog,messagebox

## Main Window Code
root=tk.Tk()
root.title("Notes App")
root.geometry("800x600")

## Creating Text Area
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica",15)
)
text.pack(expand=True,fill=tk.BOTH)

## Main Logic
###1.Function_1->To Create a New File
def new_file():
    text.delete(1.0,tk.END)

###2.Function_2-To Open New File
def opennewfile():
    # Open File Dialog
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if file_path:
        with open(file_path,"r") as NewFile:
            text.delete(1.0,tk.END)
            text.insert(tk.END,NewFile.read())

###3.Function_3->Saving The File
def save_file():
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File","*.txt")]
    )
    if file_path:
        with open(file_path,"w") as NewFile:
            NewFile.write(text.get(1.0,tk.END))
    messagebox.showinfo("Info","File Saved Successfully")

## Create Menu Bar
menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)

## NEw,OPEN,SAVE File

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=opennewfile)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

menu.add_cascade(label="File",menu=file_menu)
menu.add_cascade(label="Help",menu=file_menu)
## Starts And Keep the app open
root.mainloop()
