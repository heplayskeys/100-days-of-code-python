import os
import random
from blackjack_art import logo

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  return random.choice(CARDS)

def new_game():
  print(logo)
  dealer_hand = []
  player_hand = []
  for _ in range(2):
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
  return dealer_hand, player_hand

def calculate_score(hand):
  """Take a list of cards, and calculate a score from the values of the cards"""
  total = sum(hand)
  if 11 in hand and total > 21:
    hand[hand.index(11)] = 1
    total -= 10
  return total

def dealer_play(dealer_hand):
  dealer_score = calculate_score(dealer_hand)
  while dealer_score < 17:
    hit(dealer_hand)
    dealer_score = calculate_score(dealer_hand)

def hit(hand):
  hand.append(deal_card())

def show_cards(player, dealer):
  print(f"Your cards: {player["hand"]} -- Total: {player["score"]}")
  print(f"Computer's cards: {dealer["hand"]} -- Total: {dealer["score"]}\n")

def game_over(player_hand, dealer_hand, playing):
  player_score = calculate_score(player_hand)
  if player_score > 21:
    print("\nBUST!")
    print(f"Your cards: {player_hand} -- Total: {player_score}\n")
    return True
  elif player_score == 21 and len(player_hand) == 2:
    print("\nBLACKJACK! YOU WIN!")
    print(f"Your cards: {player_hand} -- Total: {player_score}\n")
    return True
  
  if not playing:
    dealer_score = calculate_score(dealer_hand)
    if dealer_score == 21 and len(dealer_hand) == 2:
      print("\nYOU LOSE! DEALER HAS BLACKJACK!")
    elif player_score > dealer_score or dealer_score > 21:
      print("\nYOU WIN!")
    elif player_score == dealer_score:
      print("\nIT'S A DRAW!")
    else:
      print("\nYOU LOSE!")
    
    show_cards(
      player={"hand": player_hand, "score": player_score},
      dealer={"hand": dealer_hand, "score": dealer_score}
    )
    return True
  return False

def play_game():
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system("clear")
    playing = True
    dealer, player = new_game()
  else:
    print("Goodbye\n")
    return

  if game_over(player, dealer, playing):
    return play_game()

  while playing:
    print(f"\nYour cards: {player} -- Total: {calculate_score(player)}")
    print(f"Computer's first card: {dealer[0]}\n")
    
    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
      hit(player)
    else:
      dealer_play(dealer)
      playing = False

    if game_over(player, dealer, playing):
      return play_game()
    
play_game()