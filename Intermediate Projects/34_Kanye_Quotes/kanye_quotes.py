import requests
from tkinter import *


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, width=250, text=quote, font=("Arial", 20, "bold"), fill="white")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=30, bg="light blue")

kanye = PhotoImage(file="kanye.png")
background = PhotoImage(file="background.png")

canvas = Canvas(width=300, height=414, highlightthickness=0, bg="light blue")
canvas.create_image(150, 207, image=background)
quote_text = canvas.create_text(150, 207, width=250, text="Kanye Quote", font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)
get_quote()

button = Button(image=kanye, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)

window.mainloop()



