from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=60, pady=40)

mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)

mile_label = Label(text="Miles", font=("Arial", 14, "normal"))
mile_label.grid(row=0, column=2)

text_label = Label(text="is equal to ", font=("Arial", 14, "normal"))
text_label.grid(row=1, column=0)

output_label = Label(text="0", font=("Arial", 14, "normal"))
output_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 14, "normal"))
km_label.grid(row=1, column=2)


def calculate():
    output_label.config(text=f"{round(float(mile_input.get()) * 1.60934, 2)}")


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
