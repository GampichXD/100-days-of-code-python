from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )


    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    pw_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=website, message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website,message=f"Email: {data[website]["email"]},"
                                                           f"\nPassword: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for {website} exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    username = username_entry.get()
    passwordz = pw_entry.get()
    new_data = {
        website: {
        "email": username,
        "password" : passwordz,
        }
    }
    if len(website) == 0 or passwordz == "":
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json','r') as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, 'end')
            pw_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_png = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_png)
canvas.grid(column=1,row=0)

#Website
web_label = Label(text="Website: ",justify='center')
web_label.grid(column=0,row=1, sticky='w')
web_entry = Entry(width=21)
web_entry.grid(column=1,row=1,sticky='we')
web_entry.focus()
search_button = Button(text="Search",command=find_password, width=13)
search_button.grid(column=2,row=1,sticky='we')

#Email/Username
username_label = Label(text="Email/Username: ",justify='center')
username_label.grid(column=0,row=2, sticky='w')
username_entry = Entry(width=35)
username_entry.grid(column=1,row=2,columnspan=2,sticky='we')
username_entry.insert(0, "abraham@mail.co.id")

#Password
pw_label = Label(text="Password: ",justify='center')
pw_label.grid(column=0,row=3, sticky='w')
pw_entry = Entry(width=21)
pw_entry.grid(column=1,row=3,sticky='we')
pw_button = Button(text="Generate Password",command=generate_password)
pw_button.grid(column=2,row=3,sticky='we')

#Add Button
add_button = Button(text="Add", width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky='we')




window.mainloop()



