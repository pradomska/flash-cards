from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/french_words.csv")
data = data.to_dict(orient="records")


def next_word():
    canvas.itemconfig(unknown_word, text=f"{random.choice(data)['French']}")


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=image)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
unknown_word = canvas.create_text(400, 263, text="English", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, relief="groove", command=next_word)
button_wrong.grid(row=1, column=0)

image_right = PhotoImage(file="./images/right.png")
button_right = Button(image=image_right, highlightthickness=0, relief="groove", command=next_word)
button_right.grid(row=1, column=1)

window.mainloop()
