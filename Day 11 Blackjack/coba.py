cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# computer_choice = ['y','n']
from art import logo
print("Selamat Datang di laman Game BlackJack")

import random

def ask():
    ask_to_play = input("Apakah kamu mau memainkan game BlackJack bersamaku? (y/n) : ")
    if ask_to_play == 'y':
        print("\n"*20)
        print(logo)
        print("Ayo Have Fun denganku")
        blackjack()
    else:
        print("Baiklah, terima kasih telah berkunjung")
        return

def calculate(your_own, computer_own, your_score, computer_score):
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
        if computer_score < 17:
            computer_want_add = random.choice(cards)
            computer_own.append(computer_want_add)
            computer_score += computer_want_add
        else:
            break
    return your_own, computer_own, your_score, computer_score

def normal_condition(your_score, computer_score, result):
    hasil = result
    if your_score > computer_score:
        hasil += "Menang"
    elif your_score == computer_score:
        hasil += "Seri"
    else:
        hasil += "Kalah"
    return hasil

def up_limit(own, score):
    for j in range(len(own)):
        if own[j] == 11:
            own[j] = 1
            score -= 10
    return own, score

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
    your_own, computer_own, your_score, computer_score = calculate(your_own, computer_own, your_score, computer_score)
    result = ""
    limit = 21
    if your_score > limit or computer_score > limit:
        if your_score > limit and computer_score > limit:
            your_own,your_score = up_limit(your_own,your_score)
            computer_own, computer_score = up_limit(computer_own, computer_score)
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
                result = normal_condition(your_score,computer_score,result)
        elif your_score > limit:
            your_own, your_score = up_limit(your_own, your_score)
            if your_score > limit:
                result = "Kalah"
            else:
                result = normal_condition(your_score,computer_score,result)
        elif computer_score > limit:
            computer_own, computer_score = up_limit(computer_own, computer_score)
            if computer_score > limit:
                result = "Menang"
            else:
                result = normal_condition(your_score,computer_score,result)
    else:
        result = normal_condition(your_score,computer_score,result)

    print(f"Kartu akhirmu : {your_own}, skor akhir : {your_score}")
    print(f"Kartu akhir computer : {computer_own}, skor akhir : {computer_score}")
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
        elif computer_score < limit:
            print(f"Skor kartu computer kecil banget. Kamu {result}")
        else:
            print(f"Computer Ngambil Kebanyakan. Kamu {result}")
    else:
        if computer_score == limit:
            print(f"Kamu Ngambil Kebanyakan.Computer BlackJack. Kamu {result}")
        elif your_score < limit:
            print(f"Skor kartu kamu kecil banget. Kamu {result}")
        else:
            print(f"Kamu Ngambil Kebanyakan. Kamu {result}")
    ask()


aku = ask()

















