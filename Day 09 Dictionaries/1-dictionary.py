# Dictionary in Python

# Dictionary is a collection of key-value pairs.
dictionary = {
    "key" : "value"
}

programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again."
}


print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Change the value of a key in a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again repeatedly."
print(programming_dictionary)

# Add a new item to the dictionary
empty_dictionary = {}
empty_dictionary["key"] = "value"

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)


# Edit an item in a dictionary
programming_dictionary["Bug"] = "An error in a program that prevents the program from running as expected"

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

# Grading Program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif 80 < student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 70 < student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
        
print(student_grades)


