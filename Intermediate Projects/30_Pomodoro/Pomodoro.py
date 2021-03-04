from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00", font=(FONT_NAME, 35, "bold"))
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    # convert the minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        timer_label.config(text="WORK", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
        countdown(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text="BREAK", font=(FONT_NAME, 35, "bold"), fg=RED, bg=YELLOW)
        countdown(long_break_sec)
    else:
        timer_label.config(text="BREAK", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW)
        countdown(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(number):
    minutes = floor(number / 60)
    seconds = number % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if number > 0:
        global timer
        timer = window.after(1000, countdown, number - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(0, floor(reps/2)):
            mark += "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=80, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
window.iconphoto(False, tomato_img)

"""
def say_something(thing, a, b, c):
    print(thing)
    print(a)
    print(b)
    print(c)
    
window.after(1000,
             say_something, "Hello", 3, 5, 8)  # Call function once after given time. MS specifies the time in milliseconds. FUNC gives the function which shall be called. *args are the arguments to the FUNC.
"""

# Label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Canvas Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Button
start_button = Button(text="Start", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Label
check_label = Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
