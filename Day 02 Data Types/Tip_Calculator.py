# Tip Calculator

print("Selamat datang di Tip Calculator!")
bill = float(input("Berapa total tagihan? Rp"))
tip = int(input("Berapa persen tip yang ingin Anda berikan? 10, 12, atau 15? "))
people = int(input("Berapa banyak orang yang akan membagi tagihan? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 3)
print(f"Setiap orang harus membayar: Rp{final_amount}")