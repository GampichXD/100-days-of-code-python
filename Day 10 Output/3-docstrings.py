# Docstrings in Python
# Docstrings are used to document code. 
# They are written between triple quotes.

def format_name(f_name, l_name):
    a = ("""
    Take a first and last name and format it to return the title case version of the name.
    """)
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    print(f"{formatted_f_name} {formatted_l_name}")
    return f"Hasilnya: {formatted_f_name} {formatted_l_name}"
    print("This got printed") # This line will not be printed because the return statement will exit the function

#title() --> mengubah huruf pertama dari setiap kata menjadi huruf besar

formatted_string = format_name(input("Siapa nama depanmu?"), input("Siapa nama belakangmu?")) ## return akan mereplace kode ini
print(formatted_string)