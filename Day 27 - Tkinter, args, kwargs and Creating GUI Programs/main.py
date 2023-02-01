from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()  # defaults to side = "top"
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

# Update the properties
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=2, row=2)
print(input.get()) # Returns a String


# while True:
#     listening (this is include in tkinter - window.mainloop())
window.mainloop()

# *args: Many Positional Arguments
# Unlimited Arguments
# def add(*args):
# 	for n in args:
# 		print(n)

# *args is a tuple

# **kwargs: Many Key Words Arguments

# Position Parameters
# pack() place() grid()
# cannot use geometry manager pack inside . which already has slaves managed by grid