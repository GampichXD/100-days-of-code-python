print("Selamat datang di Roler Coaster")
height = int(input("Berapa tinggi badanmu dalam cm? "))
bill = 0
if height >= 120:
    print("Kamu boleh naik roller coaster!")
    age = int(input("Berapa umurmu? "))
    if age < 12:
        bill = 5
        print("Harga tiket anak kecil adalah $5")
    elif age <= 18:
        bill = 7
        print("Harga tiket remaja adalah $7")
    else:
        bill = 12
        print("Harga tiket dewasa adalah $12")
    
    wants_photo = input("Apakah kamu ingin memesan foto? (y/n) ")
    if wants_photo == 'y':
        print("Harga foto adalah $10")
        bill += 10
    else:
        print("Terima kasih sudah berkunjung")

    print(f"Total tagihan adalah ${bill}")
else:
    print("Maaf, kamu belum boleh naik roller coaster")
