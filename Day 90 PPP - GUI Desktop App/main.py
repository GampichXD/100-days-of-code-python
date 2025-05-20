# Professional Portfolio Project - GUI Desktop App
# Disapppearing Text Writing App
# Author : Abraham
from tkinter import *
from tkinter import messagebox

# === Constants ===
TITLE_FONT = "Poppins"
WORD_FONT = "Poppins"
BACKGROUND = "#1e1e1e"
TEXT_COLOR = "#f2f2f2"
ALERT_COLOR = "#ff5555"
TIMER_COLOR = "#00ffcc"
TITLE = "#00adb5"
TIMEOUT = 5  # seconds of inactivity allowed

# === Setup window ===
root = Tk()
root.title("FlowWriter")
root.config(padx=30, pady=30, bg=BACKGROUND)
root.geometry("800x600")

# === Variables ===
count = TIMEOUT
current_text = ""


# === Functions ===
def check_text():
    global count, current_text
    typed_text = text_entry.get("1.0", END).strip()
    
    if typed_text == current_text and len(typed_text) > 0:
        timer_label.config(text=f"Inactivity: {count}", fg=ALERT_COLOR)
        if count == 0:
            text_entry.delete("1.0", END)
            timer_label.config(text="Oops! You stopped typing.", fg=ALERT_COLOR)
            messagebox.showinfo("Reset", "You stopped typing. All progress is gone!")
            count_reset()
        else:
            count_down()
    else:
        current_text = typed_text
        count_reset()

    root.after(1000, check_text)


def count_down():
    global count
    count -= 1


def count_reset():
    global count
    count = TIMEOUT
    timer_label.config(text="Keep writing...", fg=TIMER_COLOR)


# === UI Elements ===
title_label = Label(root, text="FlowWriter", font=(TITLE_FONT, 48, "bold"), fg=TITLE, bg=BACKGROUND)
title_label.pack(pady=(10, 20))

timer_label = Label(root, text="Start typing to begin...", font=(WORD_FONT, 20), fg=TIMER_COLOR, bg=BACKGROUND)
timer_label.pack(pady=(0, 20))

text_entry = Text(root, wrap=WORD, font=(WORD_FONT, 18), fg=TEXT_COLOR, bg="#2a2a2a", insertbackground=TEXT_COLOR, width=80, height=20)
text_entry.pack(padx=20, pady=10)
text_entry.focus()

# === Start Checking ===
if __name__ == "__main__":
    check_text()
    root.mainloop()

