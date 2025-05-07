# Step 2 : Replacing the blanks with Guesses


# TODO-1: - Create a "placeholder" with the same number of blanks as the word to guess.
word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(f"Kata yang dipilih: {chosen_word}")
placehlder = "_" * len(chosen_word)
print(f"Kata yang dipilih: {placehlder}")
# TODO-2: - Create a variable called 'display' to store the blanks and replace the correct blanks with the guess.
guess = input("Huruf yang ditebak: ").lower()

display = ""
for j in chosen_word:
    if j == guess:
        display += guess
    else:
        display += "_"

print(display)



# for i in chosen_word:
#     if i == guess:
#         print("Benar")
#     else:
#         print("Salah")


