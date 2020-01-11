import tkinter

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
    sub_window = tkinter.Toplevel(window)
    sub_window.title('Subprocess 1')
    lbl = tkinter.Label(sub_window, text="Subprocess 1")
    lbl.config(anchor=tkinter.CENTER)
    lbl.pack(anchor='center')
    btn = tkinter.Button(sub_window, text="OK", command=sub_window.destroy)
    btn.pack(anchor='center')

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

btn2 = tkinter.Button(window, text="Subprocess 2", command=create_subwindow2)
btn2.pack(anchor='center')


window.mainloop()

