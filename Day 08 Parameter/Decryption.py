# Caesar Chiper
## Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Ketik 'encode' untuk meng-enkripsi dan ketik 'decode' untuk men-dekripsi\n")
text = input("Ketik pesan Anda\n").lower()
shift = int(input("Ketik pergeseran angka\n"))


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position >= len(alphabet):
            new_position -= len(alphabet)
        encrypted_text += alphabet[new_position]
    print(f"Encode teks: {encrypted_text}")

# Decryption
# TODO-1: Create a function called 'decrypt' that takes the 'original_text' and 'shift_amount' as 2 inputs.
def decrypt(original_text, shift_amount):
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'encrypted_text' backwards in the alphabet by the shift amount and print the decrypted text.
    decrypted_text = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < -len(alphabet):
            new_position += len(alphabet)
        decrypted_text += alphabet[new_position]
    print(f"Decode teks: {decrypted_text}")


# TODO-3: Combine the encrypt() and decrypt() functions into a single function called caesar(). When calling the caesar() function, the user should be able to determine whether the program encodes or decodes the message by passing the 'direction' and 'text' values.
def caesar(encode_or_decode, original_text, shift_amount):
    if encode_or_decode == "encode":
        encrypt(original_text, shift_amount)
    elif encode_or_decode == "decode":
        decrypt(original_text, shift_amount)

caesar(direction, text, shift)

# Angela Yu's Solution
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
            shift_amount *= -1
    for letter in original_text:
        
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"{encode_or_decode} teks: {output_text}")

caesar(text, shift, direction)