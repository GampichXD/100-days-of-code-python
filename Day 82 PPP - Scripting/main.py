# Professional Portfolio Project - Scripting
# Text to Morse Code Converter
# Author : Abraham

# List of text 
list_text = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0',' ']

# List of morse code (by Wikipedia)
list_morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..','.-.----','..---','...--','....-','.....','-....','--...','---..','----.','-----',' ']

'''
This function can convert text to morse code. Just prepare an empty morse code variable. Fill the text argument with the text you want to convert (guess) and search index of char from the text in list_text. When you find the index, use it to get the morse code from list_morse. Add a space after each morse code to separate them. 
When you call the function, it will return the morse code, saved in morse_code variable.
'''
def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char in list_text:
            index_char = list_text.index(char)
            morse_code += list_morse[index_char] + ' '
    return morse_code

'''
This function can convert morse code to text. Just prepare an empty text variable. Fill the morse argument with the morse code you want to convert (guess) and split it by space. Then, search for the index of each morse code in list_morse. When you find the index, use it to get the text from list_text.
When you call the function, it will return the text, saved in text variable.
'''
def morse_to_text(morse):
    text = ''
    morse_list = morse.split(' ')
    for code in morse_list:
        if code in list_morse:
            index_code = list_morse.index(code)
            text += list_text[index_code]
    return text 

# Main program
while True:
    # Prompt user for input
    guess = input("Enter a text/morse code to convert to the other (or 'exit' to quit): ").upper()
    # Check if the user wants to exit
    if guess == 'EXIT':
        print("Thanks for using the converter!")
        break
    # Check if the input is valid (system identifies the input is text)
    elif all(char in list_text for char in guess):
        morse_code = text_to_morse(guess)
        print(f"Morse Code: {morse_code}")
    # Check if the input is valid (system identifies the input is morse code)
    elif all(char in list_morse for char in guess.split()):
        text = morse_to_text(guess)
        print(f"Text: {text}")
    # If the input is neither text nor morse code (or contains mix of both)
    else:
        print("Invalid input. Please enter either text or morse code.")