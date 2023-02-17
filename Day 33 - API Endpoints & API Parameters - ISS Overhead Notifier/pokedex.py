from tkinter import *
from pokemon import Pokemon

# Constants
BUTTON_BG = "#3AB47D"
SCREEN_BG = "#98CB98"

# Creating User Interface
window = Tk()
window.title("Python Pokedex")
window.minsize(width=340, height=493)
window.maxsize(width=340, height=493)

# Pokedex Canvas
canvas = Canvas(width=338, height=491, highlightthickness=0)
pokedex_img = PhotoImage(file="pokedex.png")
canvas.create_image(169, 245, image=pokedex_img)
canvas.place(x=0, y=0)

# Pokedex Entry
pokemon_entry = Entry(width=14, background=BUTTON_BG, justify="center",)
pokemon_entry.focus()
pokemon_entry.place(x=95, y=424)

window.mainloop()

pokemon = Pokemon(pokemon_entry)



