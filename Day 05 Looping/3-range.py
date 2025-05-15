# Range Function with For Loop


for number in range(1, 11,3):
    print(number)

# Gauss Challenge
total = 0
for i in range(1,101):
    total += i

print(total)

#FizzBuzz Game
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)