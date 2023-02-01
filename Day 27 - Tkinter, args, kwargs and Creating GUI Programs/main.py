from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()  # defaults to side = "top"

# Update the properties
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
input = Entry(width=10)
input.pack()
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