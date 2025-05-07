import random

friends = ["Ahmad", "Joko", "Budi", "Rudi", "Dodi"]

# Pay the bill
# Who will pay the bill?
# choice() is used to pick a random item from a list

random_in_list = random.choice(friends)
print(f"{random_in_list} yang bayar.")

# randint() is used to pick a random integer from a range
random_in_list = random.randint(0, len(friends) - 1)
print(f"{friends[random_in_list]} yang bayar.")