# Import Module
from tkinter import *
import pandas as pd
import random


# Read CSV File
index_word = {}
try:
    the_words = pd.read_csv('./data/words_to_learn.csv')
    if the_words.empty:
        raise FileNotFoundError
except (FileNotFoundError,pd.errors.EmptyDataError):
    the_words = pd.read_csv('./data/french_words.csv')
    list_words = the_words.to_dict(orient="records")
else:
    list_words = the_words.to_dict(orient="records")


def get_random_word():
    global index_word, timer
    window.after_cancel(timer)
    index_word = random.choice(list_words)
    random_word = index_word['French']
    canvas.itemconfig(lang_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=random_word, fill='black')
    canvas.itemconfig(image, image=flash_card)
    timer = window.after(3000, func=flip_card)


def flip_card():
    global timer
    canvas.itemconfig(image, image=new_flash_card)
    answer_word = index_word['English']
    canvas.itemconfig(lang_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=answer_word, fill='white')
    # timer = window.after(3000, func=get_random_word)

def known():
    list_words.remove(index_word)
    new_data = pd.DataFrame(list_words)
    new_data.to_csv('./data/words_to_learn.csv', index=False)
    get_random_word()

def unknown():
    get_random_word()






# Constant/Global Value
BACKGROUND_COLOR = "#B1DDC6"


# Background
window = Tk()
window.title("Flashy")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

# Canvas
## Flash Card
canvas = Canvas(width=800,height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card = PhotoImage(file='./images/card_front.png')
new_flash_card = PhotoImage(file='./images/card_back.png')
image = canvas.create_image(400,263,image=flash_card)
canvas.grid(column=0,row=0,columnspan=2)
## Language Text
lang_text = canvas.create_text(400,150,fill="black",font=('Arial', 40, "italic"))
## Word Text
word_text = canvas.create_text(400,263,fill="black",font=('Arial', 60, "bold"))


# Button
## Wrong
wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=unknown)
wrong_button.grid(column=0,row=1)
## Right
right_image = PhotoImage(file='./images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=known)
right_button.grid(column=1,row=1)

timer = window.after(3000, func=flip_card)
get_random_word()

window.mainloop()


