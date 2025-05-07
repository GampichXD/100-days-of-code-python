# Functions with Outputs
def my_function():
    result = 3 * 2
    return result

output = my_function() 

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"

#title() --> mengubah huruf pertama dari setiap kata menjadi huruf besar

formatted_string = format_name("angela", "YU") ## return akan mereplace kode ini
print(formatted_string)

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

function_1_output = function_2(function_1("heLLo"))
print(function_1_output)

