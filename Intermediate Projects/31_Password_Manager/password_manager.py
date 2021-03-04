from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

BG_COLOR = "#f9fadf"
FONT = ("Arial", 10, "normal")

# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #
def password_search():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="Data File Does not Exist")
    else:
        website = website_entry.get().title()
        if len(website) == 0:
            messagebox.showwarning(title="Blank Fields", message="Please Enter a Website Name")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                pyperclip.copy(password)
            else:
                messagebox.showwarning(title="Password Error", message=f"No Data for {website} Exists")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().title()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="You have Empty Fields")
    else:
        # Create a Dialogue box to make sure the data entered are correct
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details"
                        f" entered: \nEmail: {email} \nPassword: {password} \n"
                        f"Is it ok to save?")  # Returns True or False

        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)  # Reading all data, data is dictionary
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)  # Updating old data with new
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)  # Writing all data to the json file
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=50, bg=BG_COLOR)
logo = PhotoImage(file="logo.png")
window.iconphoto(False, logo)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BG_COLOR)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website: ", font=FONT, bg=BG_COLOR)
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username: ", font=FONT, bg=BG_COLOR)
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password: ", font=FONT, bg=BG_COLOR)
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=40, bg="#ced3cc")
email_username_entry = Entry(width=40, bg="#ced3cc")
password_entry = Entry(width=21, bg="#ced3cc")
email_username_entry.insert(0, "email_id@email.com")
website_entry.focus()  # Puts cursor in this text bar
website_entry.grid(row=1, column=1, columnspan=2)
email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

# Button
search_password = Button(text="Search", width=15, command=password_search, bg="#70f0b2")
generate_password = Button(text="Generate Password", command=password_generator, bg="#ddf070")
add_button = Button(text="Add", width=34, command=save_password, bg="#5a9fe0")
search_password.grid(row=1, column=2)
generate_password.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
