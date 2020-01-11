import tkinter
from tkinter import messagebox
import os

window = tkinter.Tk()

window.title("Main Window")

# create a toplevel menu
menubar = tkinter.Menu(window)
helpmenu = tkinter.Menu(menubar)

def create_about():
    about_window = tkinter.Toplevel(window)
    about_window.title('About')
    lbl = tkinter.Label(about_window, text="About")
    lbl.config(anchor=tkinter.CENTER)
    lbl.pack(anchor='center')
    btn = tkinter.Button(about_window, text="OK", command=about_window.destroy)
    btn.pack(anchor='center')

def create_subwindow1():
    def retrieve_input():
        entryText = entry.get()

        if os.path.exists(entryText):
            lbl2.config(text='A file')
        else:
            lbl2.config(text='Not a file')

    sub_window = tkinter.Toplevel(window)
    sub_window.title('Subprocess 1')
    lbl = tkinter.Label(sub_window, text="Subprocess 1")
    lbl.config(anchor=tkinter.CENTER)
    lbl.pack(anchor='center')
    btn = tkinter.Button(sub_window, text="Close", command=sub_window.destroy)
    btn.pack(anchor='center')

    lbl2 = tkinter.Label(sub_window, text="")
    lbl2.pack(anchor='center')

    entry = tkinter.Entry(sub_window)
    entry.pack(anchor='center')

    buttonCommit=tkinter.Button(sub_window, text="Check path exists",
                                command=retrieve_input)

    buttonCommit.pack(anchor='center')

    btn2 = tkinter.Button(sub_window, text="Functionality 2", command=lambda: messagebox.showinfo("Info","Not Yet Implemented"))
    btn2.pack(anchor='center')



def create_subwindow2():
    sub_window = tkinter.Toplevel(window)
    sub_window.title('Subprocess 2')
    lbl = tkinter.Label(sub_window, text="Subprocess 2")
    lbl.config(anchor=tkinter.CENTER)
    lbl.pack(anchor='center')
    btn = tkinter.Button(sub_window, text="OK", command=sub_window.destroy)
    btn.pack(anchor='center')

menubar.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="About", command=create_about)


# display the menu
window.config(menu=menubar)

btn = tkinter.Button(window, text="Subprocess 1", command=create_subwindow1)
btn.pack(anchor='center')

btn2 = tkinter.Button(window, text="Subprocess 2", command=lambda: tkinter.messagebox.showwarning("Warning","Warning message"))
btn2.pack(anchor='center')


window.mainloop()

