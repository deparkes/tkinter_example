import tkinter

window = tkinter.Tk()

window.title("Main Window")

# create a toplevel menu
menubar = tkinter.Menu(window)
helpmenu = tkinter.Menu(menubar)

def create_window():
    new_window = tkinter.Toplevel(window)
    new_window.title('About')
    lbl = tkinter.Label(new_window, text="About")
    lbl.config(anchor=tkinter.CENTER)
    lbl.pack(anchor='center')
    btn = tkinter.Button(new_window, text="OK", command=new_window.destroy)
    btn.pack(anchor='center')



menubar.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="About", command=create_window)


# display the menu
window.config(menu=menubar)

window.mainloop()

