from tkinter import *


def option_changed(*args):
    print(f"the user chose the value {variable.get()}")


master = Tk()

a = "Foo"
variable = StringVar(master)
variable.set("Apple")  # default value
variable.trace("w", option_changed)

w = OptionMenu(master, variable, "Apple", "Orange", "Grapes")
w.pack()

mainloop()
