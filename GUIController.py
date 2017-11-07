import tkinter
import tkinter.messagebox

# this function takes a input text,creates an independent frame and displays the text on desktop


def display(txt="this is a dummy text"):
    root = tkinter.Tk()
    root.withdraw()

    # this block of code generates a simple frame, sets its dimension
    #root.title("new update!")
    #root.geometry('300x100')
    # code the desired location for the frame

    #app = tkinter.Frame(root)
    #app.grid()
    # feeding the text received as parameter
    #label = tkinter.Label(app, text=txt)
    #label.grid()
    #root.mainloop()
    
    tkinter.messagebox.showinfo("NEW NOTICE!",txt)