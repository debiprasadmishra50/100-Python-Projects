from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
all_words = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    all_words = original_data.to_dict(orient="records")
else:
    all_words = data.to_dict(orient="records")

# --------------------------- CREATE FLASH CARDS ----------------------------------- #
def change_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")

def new_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(all_words)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    flip_timer = window.after(3000, func=change_card)

def knows_word():
    all_words.remove(current_word)
    data = pandas.DataFrame(all_words)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()

# --------------------------- CREATE UI ----------------------------------- #


# window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=change_card)


# Image
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Button
right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=knows_word)
wrong_button = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_word)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

new_word()
window.mainloop()
