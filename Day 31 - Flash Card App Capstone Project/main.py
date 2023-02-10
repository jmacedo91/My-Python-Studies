from tkinter import *

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LOWER_FONT = ("Arial", 40, "italic")
HIGHER_FONT = ("Arial", 60, "bold")

# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=LOWER_FONT)
canvas.create_text(400, 263, text="word", font=HIGHER_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Flash Card Buttons
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()

