import random
import my_module

# randint
random_integer = random.randint(1, 10)
print(random_integer)

# Module --> how to simplify the code
# print(my_module.my_favourite_number)

# random
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# uniform
random_float = random.uniform(1, 10)
print(random_float)

if random_float > 5:
    print("Heads")
else:
    print("Tails")







