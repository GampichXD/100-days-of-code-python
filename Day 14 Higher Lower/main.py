# Breakdown the problem
# To Do List (start with easiest)
# Turn the problem into comments
# Write code - run code - fix code
# Next Task

import random
import art
from game_data import data

logo = art.logo
vs = art.vs



def interface():
    person1 = data[random.randint(0, len(data) - 1)]
    person2 = data[random.randint(0, len(data) - 1 )]
    print(f"Bandingkan A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
    print(vs)
    print(f"Bandingkan B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
    try:
        answer = input("Siapa yang punya followers lebih? Ketik 'A' atau 'B':  ").capitalize()
        print("\n" * 50)
    except ValueError:
        print("Masukkan tebakan yang benar")
        answer = input("Siapa yang punya followers lebih? Ketik 'A' atau 'B':  ").capitalize()
    return answer, person1, person2




def game():
    score = 0
    while True:
        print(logo)
        if score != 0:
            print(f"Kamu benar, skor kamu sekarang adalah {score}")
        answer, person1, person2 = interface()
        A = person1['follower_count']
        B = person2['follower_count']
        if answer == 'A':
            if A > B :
                score += 1
            else :
                print(logo)
                print(f"Kamu salah, skor akhir kamu adalah {score}")
                break
        elif answer == 'B':
            if A < B :
                score += 1
            else :
                print(logo)
                print(f"Kamu salah, skor akhir kamu adalah {score}")
                break
    return score, person1

game()

