def great():
    print("Hello Angela")
    print("How do you do Jack?")
    print("Hello World")

great()

# Functions with Inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Angela")

def my_function(parameter):
    parameter = "argument"

# Life in Weeks
def life_in_weeks(age):
    x = (90-age)*52
    print(f"You have {x} weeks left.")

life_in_weeks(20)
    