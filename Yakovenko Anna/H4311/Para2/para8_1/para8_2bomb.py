from tkinter import  *

bomb = 100
score = 0
press_return = True


def update_display():
    pass


def is_alive():
    pass


def update_bomb():
    pass


def update_score():
    pass


def start(event):
    pass


def click():
    pass

root = Tk()
root.title("Bomb clicker")
root.geometry("600x700+1300+100")
root.iconbitmap("bomb.ico")

label = Label(root, text="Press 'Enter' to start the game", font=("Comic Sans MS", 16))
label.pack()
fuse_label = Label(root, text=f"Fuse:{str(bomb)}", font=("Comic Sans MS", 16))
fuse_label.pack()
score_label = Label(root, text=f"Score:{str(bomb)}", font=("Comic Sans MS", 16))
score_label.pack()

img_1 = PhotoImage(file="1.gif")
img_2 = PhotoImage(file="2.gif")
img_3 = PhotoImage(file="3.gif")
img_4 = PhotoImage(file="4.gif")
bomb_label = Label(image=img_1)
bomb_label.pack()

click_button = Button(root, text="Click", font=("Comic Sans MS", 25), fg="white", bg="black")
click_button.pack()



root.mainloop()