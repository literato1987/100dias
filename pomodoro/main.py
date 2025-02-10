from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    # Cancel the timer
    if timer is not None:
        window.after_cancel(timer)
    # Reset the timer text and reps
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)  # Reset title
    check_marks.config(text="")  # Clear checkmarks
    reps = 0  # Reset reps counter
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- # 
timer = None
reps = 0  # Initialize reps at the top level

def start_timer():
    global timer, reps
    # Don't start a new timer if one is already running
    if timer is not None:
        return
        
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
    update_checkmarks()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    # Dynamic typing - changing the data type during execution
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer = None
        start_timer()  # Start next session when countdown reaches 0

# Add this new function
def update_checkmarks():
    marks = ""
    completed_sessions = (reps - 1) // 2
    for _ in range(completed_sessions):
        marks += "✓"
    check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)

# Create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Create checkmark
check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_marks.grid(row=3, column=1)

# Create start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer) 
start_button.grid(row=2, column=0)

# Create reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
