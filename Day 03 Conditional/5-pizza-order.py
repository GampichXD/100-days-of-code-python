print("Selamat datang di Pizza Delivery")
size = input("Ukuran pizza yang kamu pilih? S, M, atau L ")
pepperoni = input("Apakah kamu ingin menambahkan pepperoni? Y atau N ")
extra_cheese = input("Apakah kamu ingin menambahkan keju? Y atau N ")

#work out how much they need to pay based on their size choice
bill = 0
if size == "S":
    bill += 10
elif size == "M":
    bill += 15
elif size == "L":
    bill += 20
else:
    print("Ukuran yang kamu pilih tidak tersedia")

# work out how much they need to pay based on their pepperoni choice
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# work out how much they need to pay based on their extra cheese choice
if extra_cheese == "Y":
    bill += 1


print(f"Total tagihan adalah ${bill}")