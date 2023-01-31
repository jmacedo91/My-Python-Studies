import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")  # defaults to side = "top"

import turtle

tim = turtle.Turtle()
tim.write("Some Text", font=("Times New Roman", 80, "bold"))





# while True:
#     listening (this is is include in tkinter - window.mainloop())
window.mainloop()