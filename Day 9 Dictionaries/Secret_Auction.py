# Secret Auction

# Initialization
from art import logo
print(logo)
print("Selamat datang di aplikasi lelang rahasia")
bidders = {}

# Function to find the highest bidder
def highest_bidder(bidders):
    highest_bid = 0
    for i in bidders:
        if bidders[i] > highest_bid:
            highest_bid = bidders[i]
            winner = i
    print(f"Pemenang lelang adalah {winner} dengan penawaran sebesar ${highest_bid}")

# Get the name and bid from the user
while True:
    name = input("Masukkan namamu: \n")
    bid = int(input("Masukkan penawaranmu: $\n"))
    bidders[name] = bid
    next_bidder = input("Apakah ada yang ingin menawar lagi? (y/n)\n")
    print("\n" * 100)
    if next_bidder == "n":
        highest_bidder(bidders)
        break
        
        





# Maximum value in dictionary
# max_value = max(dict, key=dict.get)