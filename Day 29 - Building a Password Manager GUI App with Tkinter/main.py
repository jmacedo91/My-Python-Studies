from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    with open("data.txt", mode="a") as data:
        data.write(f"{website} | {username} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

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
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()

username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2, sticky="W")
username_entry.insert(0, "meuemail@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="W")

# MyPass Buttons
gen_password_button = Button(text="Generate Password")
gen_password_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")


window.mainloop()