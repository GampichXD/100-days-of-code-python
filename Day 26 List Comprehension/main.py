# List Comprehension
# new_list = [new_item for item in list]

#Conditional List Comprehension
# new_list = [new_item for item in list if test]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number**2 for number in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(char) for char in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)

with open('file1.txt') as file:
   file1 = [int(a) for a in file.readlines()]
print(file1)
with open('file2.txt') as file2:
   file2 = [int(b) for b in file2.readlines()]
print(file2)
results = [[i for i in file1 for j in file2 if i == j][k] for k in range(len([i for i in file1 for j in file2 if i == j])) if [i for i in file1 for j in file2 if i == j][k] != [i for i in file1 for j in file2 if i == j][k-1] ]

# for i in file1:
#     for j in file2:
#         if i == j :
#             results.append(i)
#             break

print(results)

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value)  in dict.items() if test}
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random
students_score = {student:random.randint(1, 100) for student in names}
print(students_score)

passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
print(passed_students)
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}

print(weather_f)

# in data frame use .iterrows() di mana row bakal jadi Series
# for (index, row) in DataFrame.iterrows():
#    if row.columns == something:
#       do something
