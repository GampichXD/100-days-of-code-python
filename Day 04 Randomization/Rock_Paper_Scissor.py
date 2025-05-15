# Rock-Paper-Scissor game
## import yang dibutuhkan dan ASCII art
import random
import sys

lose = r'''
 __    __   ______   __         ______   __    __ 
|  \  /  \ /      \ |  \       /      \ |  \  |  \
| $$ /  $$|  $$$$$$\| $$      |  $$$$$$\| $$  | $$
| $$/  $$ | $$__| $$| $$      | $$__| $$| $$__| $$
| $$  $$  | $$    $$| $$      | $$    $$| $$    $$
| $$$$$\  | $$$$$$$$| $$      | $$$$$$$$| $$$$$$$$
| $$ \$$\ | $$  | $$| $$_____ | $$  | $$| $$  | $$
| $$  \$$\| $$  | $$| $$     \| $$  | $$| $$  | $$
 \$$   \$$ \$$   \$$ \$$$$$$$$ \$$   \$$ \$$   \$$
'''
win = r'''
__       __  ________  __    __   ______   __    __   ______  
|  \     /  \|        \|  \  |  \ /      \ |  \  |  \ /      \ 
| $$\   /  $$| $$$$$$$$| $$\ | $$|  $$$$$$\| $$\ | $$|  $$$$$$\
| $$$\ /  $$$| $$__    | $$$\| $$| $$__| $$| $$$\| $$| $$ __\$$
| $$$$\  $$$$| $$  \   | $$$$\ $$| $$    $$| $$$$\ $$| $$|    \
| $$\$$ $$ $$| $$$$$   | $$\$$ $$| $$$$$$$$| $$\$$ $$| $$ \$$$$
| $$ \$$$| $$| $$_____ | $$ \$$$$| $$  | $$| $$ \$$$$| $$__| $$
| $$  \$ | $$| $$     \| $$  \$$$| $$  | $$| $$  \$$$ \$$    $$
 \$$      \$$ \$$$$$$$$ \$$   \$$ \$$   \$$ \$$   \$$  \$$$$$$ 
                                                               
'''

draw = r'''
  ______   ________  _______   ______ 
 /      \ |        \|       \ |      \
|  $$$$$$\| $$$$$$$$| $$$$$$$\ \$$$$$$
| $$___\$$| $$__    | $$__| $$  | $$  
 \$$    \ | $$  \   | $$    $$  | $$  
 _\$$$$$$\| $$$$$   | $$$$$$$\  | $$  
|  \__| $$| $$_____ | $$  | $$ _| $$_ 
 \$$    $$| $$     \| $$  | $$|   $$ \
  \$$$$$$  \$$$$$$$$ \$$   \$$ \$$$$$$
'''

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Selamat datang di permainan Batu, Gunting, Kertas")
print("<=====================>")
# Pilihan user
you = int(input("Masukkan angka 0 untuk batu,\n 1 untuk gunting,\n 2 untuk kertas\n<=====================> "))

if you == 0:
    print("Kamu memilih batu")
    print(rock)
    you = rock
elif you == 1:
    print("Kamu memilih kertas")
    print(paper)
    you = paper
elif you == 2:
    print("Kamu memilih gunting")
    print(scissors)
    you = scissors
else:
    print("Input kamu salah")
    print(lose)
    sys.exit()

# Pilihan komputer
computer = [rock, paper, scissors]
computer_choice = random.choice(computer)
if computer_choice == rock:
    print("Komputer memilih batu")
    print(rock)
elif computer_choice == paper:
    print("Komputer memilih kertas")
    print(paper)
else:  
    print("Komputer memilih gunting")
    print(scissors)


# Menentukan pemenang
if you == computer_choice:
    print(draw)
elif you == rock and computer_choice == scissors:
    print(win)
elif you == paper and computer_choice == rock:
    print(win)
elif you == scissors and computer_choice == paper:
    print(win)
else:
    print(lose)


