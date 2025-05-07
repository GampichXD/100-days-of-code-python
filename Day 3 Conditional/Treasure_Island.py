# Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Selamat datang di Pulau Harta Karun")
print("Misimu adalah menemukan harta karun")
choice1 = input("Kamu berada di persimpangan jalan. Mau ke kiri atau kanan? ").lower()

if choice1 == "kiri":
    choice2 = input("Kamu sampai di danau. Ada pulau di tengah"
                     " danau. Mau menunggangi perahu (ketik \"tunggu\" untuk" 
                     " menunggu perahu) atau berenang (ketik" 
                     " \"renang\" jika ingin langsung berenang)? ").lower()
    if choice2 == "tunggu":
        choice3 = input("Kamu menunggu perahu dan akhirnya sampai di pulau." 
              " Di pulau tersebut ada 3 pintu dengan warna"
              " yang berbeda yakni merah, kuning, dan biru." 
              " Pintu mana yang akan kamu pilih? ").lower()
        if choice3 == "merah":
            print("Ruangan itu penuh api! Kamu terbakar Game Over!")
        elif choice3 == "kuning":
            print("Ruangan itu penuh harta karun! Kamu menemukan harta karun! Selamat!")
        elif choice3 == "biru":
            print("Ruangan itu penuh binatang buas! Kamu dimangsa! Game Over!")
        else:
            print("Kamu memilih pintu yang tidak ada. Game Over!")
    else:
        print("Kamu diserang oleh buaya. Game Over!")
else:
    print("Kamu jatuh ke jurang. Game Over!")



