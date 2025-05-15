    # TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
print("Selamat datang di Caesar Chiper")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']





def caesar(original_text, shift_amount, encode_or_decode, list_text):
# TODO-2: What happen if the user enters a number/symbol/space?
    # tipe_text = True
    # while tipe_text:
    #     for i in original_text:
    #         if i == " " or i in number or i in symbol:
    #             print("Mohon masukkan huruf saja")
    #             original_text = input("Ketik pesan Anda\n").lower()
    #         else: 
    #             tipe_text = False
    output_text = ""
    if encode_or_decode == "decode":
            shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"{encode_or_decode}d teks: {output_text}")
    list_text.append(output_text)


    # TODO-3: Can you figure out a way to restart the chiper program?
list_text = []

while True:
    direction = input("Ketik 'encode' untuk meng-enkripsi dan keik 'decode' untuk men-dekripsi\n")
    text = input("Ketik pesan Anda\n").lower()
    shift = int(input("Ketik pergeseran angka\n"))

    caesar(text, shift, direction, list_text)
    restart = input("Apakah Anda ingin mengulangi program?(y/n)\n")
    if restart == "n":
        break

print("Berikut adalah list text yang sudah dienkripsi atau didekripsi")
print(list_text)