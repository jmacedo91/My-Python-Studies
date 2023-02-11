from tkinter import *
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LOWER_FONT = ("Arial", 40, "italic")
HIGHER_FONT = ("Arial", 60, "bold")
current_card = {}
data = None

# --------------------- CREATE NEW FLASH CARDS ------------------------ #
try:
	data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
	data = pd.read_csv("data/french_words.csv")
finally:
	to_learn = data.to_dict(orient="records")


def next_card():
	global current_card, flip_timer
	window.after_cancel(flip_timer)
	current_card = random.choice(to_learn)
	canvas.itemconfig(card_title, text="French", fill="black")
	canvas.itemconfig(card_word, text=current_card["French"], fill="black")
	canvas.itemconfig(card_background, image=card_front_img)
	flip_timer = window.after(3000, flip_cards)


def is_known():
	to_learn.remove(current_card)
	words_to_learn = pd.DataFrame(to_learn)
	words_to_learn.to_csv("data/words_to_learn.csv", index=False)
	next_card()


def flip_cards():
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=current_card["English"], fill="white")
	canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- UI SETUP ------------------------------- #


# Window Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_cards)

# Flash Card Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=LOWER_FONT)
card_word = canvas.create_text(400, 263, text="", font=HIGHER_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Flash Card Buttons
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, command=is_known, highlightthickness=0)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
