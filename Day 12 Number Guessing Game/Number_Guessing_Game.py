# TODO-1: Function to welcoming and ask for the type of game
import random
from art import logo
def ask():
    print(logo)
    print("Selamat Datang di Permainan Tebak Angka")
    print("Aku telah memilih angka acak dari di antara 1 dan 100. Tebaklah")
    number = []
    for i in range(100):
        number.append(i)
    guess = random.choice(number)
    choose = input("Pilih mode difficulty (easy / hard) : ")
    attempt = 0
    if choose == 'easy':
        attempt += 10
    else:
        attempt += 5
    return attempt, guess

# TODO-2: Function to guess the number
def guess_number():
    while True:
        attempt, guess = ask()
        while attempt > 0:
            print(f"Kamu memiliki {attempt} kesempatan untuk menebak angka pilihanku")
            guessing = int(input("Tebaklah : "))
            if guessing > guess:
                print("Terlalu Tinggi")
                attempt -= 1
            elif guessing < guess:
                print("Terlalu rendah")
                attempt -= 1
            else:
                print(f"Tebakanmu benar, angka yang ku pilih adalah {guess}")
                break
        if attempt == 0:
            print(f"Kesempatanmu habis. Angka yang ku pilih adalah {guess}")
        last_play = f"Angka terakhir yang seharusnya kamu tebak adalah {guess} dengan sisa kesempatan adalah {attempt}"
        play_again = input("Apakah kamu ingin bermain lagi? (y/n) : ")
        if play_again != 'y':
            print("Terima kasih telah bermain")
            break
    return last_play

main = guess_number()
print(main)


