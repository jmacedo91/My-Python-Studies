from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

# Button
def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Button 1", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Button 2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get()) # Returns a String

window.mainloop()