from tkinter import *
from tkinter import messagebox
import requests.exceptions
from pokemon import Pokemon
import urllib.request

# Constants
ENTRY_BG = "#3AB47D"
SCREEN_BG = "#98CB98"
BUTTON_BG = "#585858"

# Creating User Interface
window = Tk()
window.title("Python Pokedex")
window.minsize(width=340, height=493)
window.maxsize(width=340, height=493)

# Pokédex Canvas
pokedex_canvas = Canvas(width=338, height=491, highlightthickness=0)
pokedex_img = PhotoImage(file="pokedex.png")
pokedex_canvas.create_image(169, 245, image=pokedex_img)
pokedex_canvas.place(x=0, y=0)

# Pokédex Entry
pokemon_entry = Entry(width=14, background=ENTRY_BG, justify="center")
pokemon_entry.place(x=97, y=424)
pokemon_entry.focus()

# Pokedex Info
name = Label(text="Name:", bg=SCREEN_BG, font=("Arial", 10, "bold"))
name.place(x=82, y=245)

number = Label(text="ID:", bg=SCREEN_BG, font=("Arial", 10, "bold"))
number.place(x=82, y=265)

element = Label(text="Element:", bg=SCREEN_BG, font=("Arial", 10, "bold"))
element.place(x=82, y=285)

# Pokedex Button


def search():
    pokemon_name = pokemon_entry.get().lower()
    try:
        pkm = Pokemon(pokemon_name)
    except requests.exceptions.JSONDecodeError:
        messagebox.showerror(title="Not Found!", message="This Pokémon doesn't exist! Please, review entries!")
        name.config(text=f"Name: Not Found!")
        number.config(text=f"ID: Not Found!")
        element.config(text=f"Element: Not Found!")
    else:
        name.config(text=f"Name: {pkm.specie}")
        number.config(text=f"ID: {pkm.id}")
        element.config(text=f"Element: {pkm.type}")
        pokemon_canvas = Canvas(width=96, height=96, highlightthickness=0)
        urllib.request.urlretrieve(f"{pkm.get_sprite()}", f"pokemon_sprites/{pkm.id}-{pkm.specie}.png")
        pokemon_img = PhotoImage(file=f"pokemon_sprites/{pkm.id}-{pkm.specie}.png")
        pokemon_canvas.create_image(96, 96, image=pokemon_img)
        pokemon_canvas.place(x=120, y=153)


pokedex_btn = Button(text="Search", command=search, bg=BUTTON_BG, fg="white")
pokedex_btn.place(x=118, y=460)

window.mainloop()
