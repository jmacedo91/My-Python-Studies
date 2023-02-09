from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)  # Write a new dictionary open("data.json", mode="w")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get().title()
    if website == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Fail", message="No Data File Found")
        else:
            if website in data:
                messagebox.showinfo(title="Success", message=f"Username: {data[website]['username']}"
                                                             f"\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Fail", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# MyPass Canvas
canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

# MyPass Labels 🏷
website_label = Label(text="Website:", justify="center")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", justify="center")
password_label.grid(row=3, column=0)

# MyPass Entries 📝
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()

username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2, sticky="W")
username_entry.insert(0, "meuemail@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="W")

# MyPass Buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")


window.mainloop()
