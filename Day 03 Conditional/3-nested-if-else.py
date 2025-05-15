print("Selamat datang di Roler Coaster")
height = int(input("Berapa tinggi badanmu dalam cm? "))

if height >= 120:
    print("Kamu boleh naik roller coaster!")
    age = int(input("Berapa umurmu? "))
    if age < 12:
        print("Harga tiket adalah $5")
    elif age <= 18:
        print("Harga tiket adalah $7")
    else:
        print("Harga tiket adalah $12")
else:
    print("Maaf, kamu belum boleh naik roller coaster")

# BMI Calculator 2.0
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")