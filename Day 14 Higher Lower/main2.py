import random
import art
from game_data import data

logo = art.logo
vs = art.vs

def data_format(person):
    person_name = person["name"]
    person_desc = person["description"]
    person_country = person["country"]
    return f"{person_name}, a {person_desc}, from {person_country}"

def compare(person1, person2):
    if person1["follower_count"] > person2["follower_count"]:
        return "A"
    else:
        return "B"

person2 = random.choice(data)
score = 0
while True:
    person1 = person2
    person2 = random.choice(data)
    while person1 == person2:
        person2 = random.choice(data)
    print("\n" * 100)
    print(logo)
    if score != 0:
        print(f"Benar! Skor kamu sekarang adalah {score}")
    print(f"Bandingkan A: {data_format(person1)}")
    print(vs)
    print(f"Bandingkan B: {data_format(person2)}")
    guess = input("Siapa yang memiliki lebih banyak follower? A atau B: ").upper()
    if guess == "A":
        if compare(person1, person2) == "A":
            score += 1
        else:
            print("\n" * 100)
            print(logo)
            print(f"Salah! Skor akhir kamu adalah {score}")
            break
    else:
        if compare(person1, person2) == "B":
            score += 1
        else:
            print("\n" * 100)
            print(logo)
            print(f"Salah! Skor akhir kamu adalah {score}")
            break














