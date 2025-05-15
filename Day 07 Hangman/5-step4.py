# Step 5 : Improving the User Interface



# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

import random
from hangman_words import word_list
import hangman_art

# word_list = word_list

lives = 6

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


logo = hangman_art.logo
print(logo)
chosen_word = random.choice(word_list)

# print(f"Kata yang dipilih: {chosen_word}")
placeholder = "_" * len(chosen_word)
print(f"Kata yang dipilih: {placeholder}")

    

      
# TODO-2: - Update the code to use the stages from the file hangman_art.py
stages = hangman_art.stages
# Angela Yu's Solution
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter:").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        
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

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(lose)

    if "_" not in display:
        game_over = True
        print(win)

    print(stages[lives])
    print(f"Lives left: {lives}")

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.



# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
# we should not deduct a life fot this.
# e.g. you've already guessed 'a'.

# TODO-5: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# e.g. you've guessed 'o', but the word is not 'o'. You lose a life.
# TODO-6: Update the code below to tell the user how many lives they have left.
# TODO-7: Update the print to give the user the correct 