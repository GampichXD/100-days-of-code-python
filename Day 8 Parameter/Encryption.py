# Caesar Chiper
## Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Ketik 'encode' untuk meng-enkripsi dan ketik 'decode' untuk men-dekripsi\n")
text = input("Ketik pesan Anda\n").lower()
shift = int(input("Ketik pergeseran angka\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'original_text' forwards in the alphabet by the shift amount and print the encrypted text.
    encrypted_text = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code to keep the code?
        if new_position >= len(alphabet):
            new_position -= len(alphabet)
        encrypted_text += alphabet[new_position]
    print(f"Encode teks: {encrypted_text}")



# TODO-3: Call the 'encrypt' function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == "encode":
    encrypt(text, shift)