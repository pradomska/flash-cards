import sys
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
word = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    messagebox.showinfo(title="Change list", message="List of words to learn is empty,\nadd new list of words.")
    sys.exit()
else:
    to_learn = data.to_dict(orient="records")


def next_word():
    global word, flip_timer

    window.after_cancel(flip_timer)
    if to_learn:
        word = random.choice(to_learn)
        canvas.itemconfig(canvas_image, image=image_front)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(unknown_word, text=f"{word['French']}", fill="black")
        flip_timer = window.after(3000, func=flip_card)
    else:
        messagebox.showinfo(title="You are smart!", message="List of words to learn is empty")
        window.destroy()

def known_word():
    global to_learn

    to_learn.remove(word)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_word()


def flip_card():
    canvas.itemconfig(canvas_image, image=image_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(unknown_word, text=f"{word['English']}")


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_back = PhotoImage(file="./images/card_back.png")
image_front = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=image_front)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
unknown_word = canvas.create_text(400, 263, text="English", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, relief="groove", command=next_word)
button_wrong.grid(row=1, column=0)

image_right = PhotoImage(file="./images/right.png")
button_right = Button(image=image_right, highlightthickness=0, relief="groove", command=known_word)
button_right.grid(row=1, column=1)

next_word()

window.mainloop()
