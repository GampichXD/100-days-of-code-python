from tkinter import *



window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=210,height=70)
window.config(padx=20,pady=20)

def convert():
    first_value = float(miles_entry.get())
    result_value = str(round(first_value * 1.60934))
    # print("It's clicked")
    km_result.config(text=result_value)


miles_entry = Entry(width=7)
miles_entry.grid(column=1,row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)
equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)
km_result = Label(text="0", justify='center')
km_result['text'] = "0"
km_result.grid(column=1,row=1)
km_label = Label(text="Km")
km_label.grid(column=2,row=1)





calculate_button = Button(text="Calculate",command=convert)
calculate_button.grid(column=1,row=2)











window.mainloop()