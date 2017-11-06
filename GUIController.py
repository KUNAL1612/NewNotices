from tkinter import *

# this function takes a input text,creates an independent frame and displays the text on desktop
def display(txt="this is a dummy text"):
    root = Tk()

    # this block of code generates a simple frame, sets its dimension
    root.title("new update!")
    root.geometry('300x100')
    # code the desired location for the frame

    app = Frame(root)
    app.grid()
    # feeding the text received as parameter
    label = Label(app, text=txt)
    label.grid()
    root.mainloop()