import threading
from tkinter import *
import winsound
import threading
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

# ---------------------------- EXTRA------------------------------- #


def pop_app_up():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_canvas, text='00:00')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        reps = 0
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM -------------------------------


def count_down(count):
    global timer
    canvas.itemconfig(timer_canvas, text=f"{count//60:02d}:{count%60:02d}")
    if count == 0:
        sound_thread = threading.Thread(target=pop_app_up)
        sound_thread.start()
        start_timer()
        if reps % 2 == 0:
            check_marks.config(text=f"{'✔'*int(reps/2)}")

    elif count > 0:
        timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT_NAME)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

window.mainloop()
