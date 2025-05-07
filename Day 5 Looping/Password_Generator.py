import random
# Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Selamat datang di Password Generator!")
nr_letters = int(input("Berapa banyak huruf yang Anda inginkan dalam password Anda?\n"))
nr_symbols = int(input(f"Berapa banyak simbol yang Anda inginkan?\n"))
nr_numbers = int(input(f"Berapa banyak angka yang Anda inginkan?\n"))

password_list = []
for char in range(nr_letters):
    password_list.append(random.choice(letters))
for char in range(nr_symbols):
    password_list += random.choice(symbols)
for char in range(nr_numbers):
    password_list += random.choice(numbers)

print(password_list)


your_password = ""
for char in range(len(password_list)):
    your_password += random.choice(password_list)

print(f"Password Anda adalah: {your_password}")

#random.shuffle(password_list)