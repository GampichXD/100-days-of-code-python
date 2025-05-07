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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_min)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(long_break_min)
    else:
        timer_label.config(text="Break", fg=RED)
        count_down(short_break_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = format(math.floor(count / 60),'02d')
    count_sec = format(count % 60, '02d')

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for step in range(work_session):
            marks += "✓"
        check_mark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)
# count_down(5)

# Button
button_start = Button(text="Start",highlightthickness=0, command=start_timer)
button_start.grid(column=0,row=2)
button_reset = Button(text="Reset",highlightthickness=0, command=reset_timer)
button_reset.grid(column=2,row=2)

# Text Label
check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME,12,"bold"))
check_mark.grid(column=1,row=3)
timer_label = Label(text="Timer",bg=YELLOW,fg=GREEN, font=(FONT_NAME,50))
timer_label.grid(column=1,row=0)

window.mainloop()





