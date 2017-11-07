import tkinter
import tkinter.messagebox

# this function takes a input text,creates an independent frame and displays the text on desktop


def display(txt="this is a dummy text"):
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo("NEW NOTICE!",txt)
