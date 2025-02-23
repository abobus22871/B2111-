from tkinter import *
from random import choice


def click():
    color = choice(["red", "tomato", "gold", "magenta"])
    window["bg"] = color

window = Tk()
window.title("My Window")
window.geometry("500x200+1200+100")
window.resizable(False, False)
nap1 = Label(text="Test text", font=("Comic Sans MS", 25))
nap1.pack()
but1 = Button(text="Click", font=("Comic Sans MS", 25), command=click)
but1.pack()
window.mainloop()
