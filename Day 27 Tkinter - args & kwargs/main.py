"""
GUI --> Graphical User Interface
Mac Lisa is first GUI
Window from Microsoft
"""

from tkinter import *

from PIL.ImageOps import expand
from bokeh.layouts import column

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)


#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.place(x=100,y=200)
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)

my_label['text'] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    print("I got clicked")
    # change = the_input.get()
    # my_label.config(text=change)



button = Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1,row=1)

new_button = Button(text="New Button")
new_button.grid(column=2,row=0)

#Entry

the_input = Entry(width=10)
# the_input.pack(side="left")
the_input.grid(column=3,row=2)
print(the_input.get())

# import turtle
#
# tim = turtle.Turtle()
# tim.write("Some text")





window.mainloop()










