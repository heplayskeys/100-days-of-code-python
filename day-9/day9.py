import blind_auction_art as ba_art
import os

print(ba_art.logo)
print("Welcome to the secret auction program.")

bids = {}
continue_bidding = True

def find_highest_bidder():
  top_bid = 0
  winner = ""
  for name in bids:
    if bids[name] > top_bid:
      top_bid = bids[name]
      winner = name
  print(f"The winner is {winner} with a bid of ${top_bid}")


while continue_bidding:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  bids[name] = bid

  if more_bids == "no":
    continue_bidding = False
    find_highest_bidder()
  elif more_bids == "yes":
    os.system("clear")
