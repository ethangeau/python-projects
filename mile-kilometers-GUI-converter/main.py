from tkinter import *

FONT = ("Arial", 20, "normal")


def converter():
    miles = float(entry.get())
    kilometers = str(round(miles * 1.609, 2))
    result_label.config(text=kilometers)


window = Tk()
window.title('Mile to Km Converter')
window.config(padx=30, pady=30)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

entry = Entry(width=10, font=FONT)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

result_label = Label(font=FONT)
result_label.grid(column=1, row=1)

button = Button(text="Calculater", command=converter, font=("Arial", 20, "normal"))
button.grid(column=1, row=2)

window.mainloop()
