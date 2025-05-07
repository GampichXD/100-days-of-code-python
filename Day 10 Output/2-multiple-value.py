

def format_name(f_name, l_name):
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




#Lap Year
def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    leap_year = []
    is_leap_year = False
    if year % 4 == 0:
        leap_year.append("Leap")
    else:
        leap_year.append("Not Leap")
    if year % 100 != 0:
        leap_year.append("Leap")
    else:
        leap_year.append("Not Leap")
    if year % 400 == 0:
        leap_year.append("Leap")
    else:
        leap_year.append("Not Leap")
    for i in range(len(leap_year)):
        if leap_year[2] == "Leap":
            is_leap_year = True
        elif leap_year[0] == "Leap" and leap_year[1] == "Leap":
            is_leap_year = True
    return is_leap_year
        
a_year = is_leap_year(2000)
print(a_year)

def is_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

a_year = is_leap_year(2000)
print(a_year)  # Output: True
        