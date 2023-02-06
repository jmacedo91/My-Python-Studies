from tkinter import *
from playsound import playsound
import time

# ---------------------------- CONSTANTS ------------------------------- #
BG_COLOR = "#EAEAEA"
# ---------------------------- TRANSLATOR ------------------------------- #
MORSE_CODE_DICT = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....',
            'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-',
            'U': '..-', 'V': '...-',
            'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----',
            '2': '..---', '3': '...--',
            '4': '....-', '5': '.....',
            '6': '-....', '7': '--...',
            '8': '---..', '9': '----.',
            ' ': '/'
        }

def translate():
    user_entry = string_entry.get().upper()
    translated_text = ""
    for char in user_entry:
        translated_text += (MORSE_CODE_DICT[char] + " ")
    morse_code.config(text=translated_text)

def play_sound():
    for code in morse_code["text"]:
        if code == ".":
            playsound("short_beep.mp3")
            time.sleep(0.05)
        elif code == "-":
            playsound("long_beep.mp3")
            time.sleep(0.05)
        elif code == "/" or code == " ":
            time.sleep(0.15)
        else:
            print("Invalid character!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Morse Code Translator")
window.config(padx=100, pady=30, bg=BG_COLOR)


# Morse Canvas
canvas = Canvas(width=256, height=256, bg=BG_COLOR, highlightthickness=0)
morse_img = PhotoImage(file="codigo-morse.png")
canvas.create_image(128, 128, image=morse_img)
canvas.grid(row=1, column=1)

# Labels
logo_label = Label(text="Morse Code Translator", background=BG_COLOR, font=("Arial", 20, "bold"))
logo_label.grid(row=0, column=1)

string_label = Label(text="Input your text:", background=BG_COLOR, font=("Arial", 12, "bold"))
string_label.grid(row=2, column=0)

output_label = Label(text="Your Output Code:", background=BG_COLOR, font=("Arial", 12, "bold"))
output_label.grid(row=3, column=0)
output_label.config(pady=10)

morse_code = Label(text="", background=BG_COLOR, font=("Arial", 16, "bold"))
morse_code.grid(row=3, column=1)

# Entry
string_entry = Entry(width=30, font=("Arial", 12, "bold"))
string_entry.grid(row=2, column=1)
string_entry.focus()

# Button
convert_btn = Button(text="Translate", font=("Arial", 12, "bold"), command=translate)
convert_btn.grid(row=2, column=2)

sound_btn = Button(text="Play Sound", font=("Arial", 12, "bold"), command=play_sound)
sound_btn.grid(row=3, column=2)

window.mainloop()
