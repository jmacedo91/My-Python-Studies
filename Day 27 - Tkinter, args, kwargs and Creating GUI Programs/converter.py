from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

# Entry Value
entry = Entry(width=7)
entry.insert(END, string=0)
entry.grid(column=1, row=0)

# Entry Label
entry_label = Label(text="Miles")
entry_label.grid(column=2, row=0)

# Output Labels
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

value_label = Label(text=0)
value_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

# Calculate Button
def converter():
	miles = entry.get()
	kilometers = round(1.60934 * float(miles), 2)
	new_value = str(kilometers)
	value_label.config(text=new_value)

button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)



window.mainloop()