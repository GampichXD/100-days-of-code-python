# Step 3 : Checking if the player has won

# TODO-1: - Use a while loop to let the user guess again.
word_list = ["aardvark", "baboon", "camel"]
import random

chosen_word = random.choice(word_list)

print(f"Kata yang dipilih: {chosen_word}")
placeholder = "_" * len(chosen_word)
print(f"Kata yang dipilih: {placeholder}")
# while True:
#     guess = input("Huruf yang ditebak: ").lower()
#     if len(guess) != 1:
#         print("Masukkan hanya 1 huruf")
#         continue



# Solusi Mandiri
# display = ["_"] * len(chosen_word)
# kosong = ""
# while True:
#     guess = input("Huruf yang ditebak: ").lower()
#     if len(guess) != 1:
#         print("Masukkan hanya 1 huruf")
#         continue
#     for k in range(len(chosen_word)):
#         if guess == chosen_word[k]:
#             display[k] = guess
#     for l in display:
#         kosong += l
#     print(kosong)
#     if "_" in kosong:
#         kosong = ""
#         continue
#     else:
#         print("Kamu menang")
#         break
    

        




    
# TODO-2: - Change the for loop so that you keep the previous correct guesses and the blanks in the word.





# display = ""
# while True:
#     for j in chosen_word:
#         if j == guess:
#             display += guess
#         else:
#             display += "_"
#         print(display)

# Angela Yu's Solution
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter:").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("Kamu menang")




# for i in chosen_word:
#     if i == guess:
#         print("Benar")
#     else:
#         print("Salah")