cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_choice = ['y','n']
from art import logo
print("Selamat Datang di laman Game BlackJack")

import random

def ask():
    ask_to_play = input("Apakah kamu mau memainkan game BlackJack bersamaku? (y/n) : ")
    if ask_to_play == 'y':
        print("\n"*20)
        print(logo)
        print("Selamat Datang di Permainan BlackJack")
        blackjack()
    else:
        print("Baiklah, terima kasih telah berkunjung")
        return

def blackjack():
    your_own = []
    computer_own = []
    for i in range(2):
        your_own.append(random.choice(cards))
        computer_own.append(random.choice(cards))
    your_score = 0
    computer_score = 0
    for i in your_own:
        your_score += i
    for i in computer_own:
        computer_score += i
    while True:
        print(f"Kartu-mu: {your_own}, skor sekarang: {your_score}")
        print(f"kartu pertama komputer adalah {computer_own[0]}")
        ask_to_add = input(f"Apakah kamu ingin menambah kartu? (y/n)")
        if ask_to_add == 'y':
            your_add = random.choice(cards)
            your_own.append(your_add)
            your_score += your_add
        else:
            break
    while True:
        computer_add = random.choice(computer_choice)
        if computer_add == 'y':
            computer_want_add = random.choice(cards)
            computer_own.append(computer_want_add)
            computer_score += computer_want_add
        else:
            break
    print(f"Kartu akhirmu : {your_own}, skor akhir : {your_score}")
    print(f"Kartu akhir computer : {computer_own}, skor akhir : {computer_score}")
    result = ""
    limit = 21
    if your_score > limit or computer_score > limit:
        if your_score > limit and computer_score > limit:
            for j in your_own:
                if j == 11:
                    j = 1
                    your_score -= 10
            for k in computer_own:
                if k == 11:
                    k = 1
                    computer_score -= 10
            if your_score > limit and computer_score > limit:
                if your_score < computer_score:
                    result = "Menang"
                elif your_score == computer_score:
                    result = "Seri"
                else:
                    result = "Kalah"
            elif your_score > limit:
                result = "Kalah"
            elif computer_score > limit:
                result = "Menang"
            elif your_score == computer_score:
                result = "Seri"
            else:
                if your_score > computer_score:
                    result = "Menang"
                elif your_score == computer_score:
                    result = "Seri"
                else:
                    result = "Kalah"
        elif your_score > limit:
            for j in your_own:
                if j == 11:
                    j = 1
                    your_score -= 10
            if your_score > limit:
                result = "Kalah"
            else:
                if your_score > computer_score:
                    result = "Menang"
                elif your_score == computer_score:
                    result = "Seri"
                else:
                    result = "Kalah"
        elif computer_score > limit:
            for k in computer_own:
                if k == 11:
                    k = 1
                    computer_score -= 10
            if computer_score > limit:
                result = "Menang"
            else:
                if your_score > computer_score:
                    result = "Menang"
                elif your_score == computer_score:
                    result = "Seri"
                else:
                    result = "Kalah"
    else:
        if your_score > computer_score:
            result = "Menang"
        elif your_score == computer_score:
            result = "Seri"
        else:
            result = "Kalah"
    judge(result, your_score, computer_score, limit)
    return result

def judge(result, your_score, computer_score, limit):
    if result == "Seri":
        if your_score == limit and computer_score == limit:
            print(f"Kamu dan Computer sama-sama BlackJack. Kalian {result}")
        else:
            print(f"Kamu dan Computer sama-sama imbang. Kalian {result}")
    elif result == "Menang":
        if your_score == limit:
            print(f"Computer Ngambil Kebanyakan.Kamu BlackJack. Kamu {result}")
        else:
            print(f"Computer Ngambil Kebanyakan. Kamu {result}")
    else:
        if computer_score == limit:
            print(f"Kamu Ngambil Kebanyakan.Computer BlackJack. Kamu {result}")
        else:
            print(f"Kamu Ngambil Kebanyakan. Kamu {result}")
    ask()


ask()

















