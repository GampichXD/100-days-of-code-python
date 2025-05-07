# Step 1 : Picking a random word and checking the answer

# TODO-1: - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}")
# TODO-2: - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Huruf yang ditebak: ").lower()
# TODO-3: - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in chosen_word:
    if i == guess:
        print("Benar")
    else:
        print("Salah")