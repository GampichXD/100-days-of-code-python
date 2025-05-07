# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# Positional Arguments
greet_with("Angela","London")

# Keyword Arguments
greet_with(location="NewYork",name="Jack")

a = "Aku"
b = "Kamu"
total_a = 0
total_bukan_a = 0
for i in a:
    if i == "A" or i == "a":
        total_a += 1
    else:
        total_bukan_a += 1
print(f"Total huruf A: {total_a} dan total bukan huruf A: {total_bukan_a}")

# Love Calculator
def calculate_love_score(name1, name2):
    first_digit = 0
    second_digit = 0
    for true in name1:
        if true == "t" or true == "T":
            first_digit += 1
        elif true == "r" or true == "R":
            first_digit += 1
        elif true == "u" or true == "U":
            first_digit += 1
        elif true == "e" or true == "E":
            first_digit += 1
            second_digit += 1
        elif true == "l" or true == "L":
            second_digit += 1
        elif true == "o" or true == "O":
            second_digit += 1
        elif true == "v" or true == "V":
            second_digit += 1
        else:
            first_digit += 0
            second_digit += 0
    for love in name2:
        if love == "t" or love == "T":
            first_digit += 1
        elif love == "r" or love == "R":
            first_digit += 1
        elif love == "u" or love == "U":
            first_digit += 1
        elif love == "e" or love == "E":
            first_digit += 1
            second_digit += 1
        elif love == "l" or love == "L":
            second_digit += 1
        elif love == "o" or love == "O":
            second_digit += 1
        elif love == "v" or love == "V":
            second_digit += 1
        else:
            first_digit += 0
            second_digit += 0
    love_score = first_digit*10 + second_digit
    print(love_score)

calculate_love_score("Ema","Ama")