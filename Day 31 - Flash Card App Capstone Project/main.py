from tkinter import *
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LOWER_FONT = ("Arial", 40, "italic")
HIGHER_FONT = ("Arial", 60, "bold")

# --------------------- CREATE NEW FLASH CARDS ------------------------ #
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
	current_card = random.choice(to_learn)
	canvas.itemconfig(card_title, text="French")
	canvas.itemconfig(card_word, text=current_card["French"])

# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=LOWER_FONT)
card_word = canvas.create_text(400, 263, text="", font=HIGHER_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Flash Card Buttons
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, command=next_card, highlightthickness=0)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()

