import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")  # defaults to side = "top"


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