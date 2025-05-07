#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
# list_name = []
# with open('./input/Names/invited_names.txt',"r") as file:
#     for name in file:
#         list_name.append(name.rstrip())
#         # print(name)
# print(list_name)
#
#
#
# list_letter = []
#
# #Replace the [name] placeholder with the actual name.
# for name in list_name:
#     with open("./Input/Letters/starting_letter.txt", "r") as file:
#
#         # letter = file.readline().replace("[name]",a_name)
#     #     print(letter)
#     #     list_a_letter.append(letter)
#     #     list_letter.append(list_a_letter):
#         new_letter = (file.read().replace("[name]",name)).rstrip()
#         list_letter.append(new_letter)
#
#
#
#
# print(list_letter)
#
# #Save the letters in the folder "ReadyToSend".
# for name,letter in enumerate(list_letter):
#      with open(f"./Output/ReadyToSend/letter_for_{list_name[name]}.txt",'w') as file :
#          file.write(letter)
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Live to Send
PLACEHOLDER = "[name]"
with open('./Input/Names/invited_names.txt') as file:
    list_name = file.readlines()
    # print(list_name)

with open("./Input/Letters/starting_letter.txt") as file:
    new_letter = file.read()
    # print(new_letter)
    for name in list_name:
        strip_name = name.strip()
        correct_letter = new_letter.replace(PLACEHOLDER,strip_name)
        # print(correct_letter)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt",'w') as sending_file:
            sending_file.write(correct_letter)




