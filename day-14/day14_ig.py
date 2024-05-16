import os
from random import choice
from higher_or_lower_art import logo, versus
from game_data import data

def play_round(account_a, score=0):
  if score > 0:
    print(f"You're right! Current score: {score}")

  round_accounts = {
    'A': account_a,
  }
  show_info(account_a, 'A')
  print(versus)
  account_b = pick_account()

  while account_a == account_b:
    account_b = pick_account()

  round_accounts['B'] = account_b
  show_info(account_b, 'B')
  guess = make_guess()
    
  if guess_correct(account_a['follower_count'], account_b['follower_count'], guess):
      score += 1
      os.system("clear")
      print(logo)
      return play_round(round_accounts[guess], score)
  else:
    correct_answer = account_b if guess == "A" else account_a
    print(f"WRONG! It was {correct_answer['name']} with {correct_answer['follower_count']} million followers.")
    print(f"You scored {score} {'points' if score > 1 else 'point'}.")
  return start()

def pick_account():
  return choice(data)

def show_info(account, ltr):
  print(f"{'Compare' if ltr == 'A' else 'Against'} {ltr}: {account['name']}, a {account['description']}, from {account['country']}.")

def make_guess():
  return input("Who has more followers? Type 'A' or 'B': ").upper()

def guess_correct(account_a_followers, account_b_followers, guess):
  if (account_a_followers > account_b_followers):
    return guess == "A"
  else:
    return guess == "B"

def start():
  if input("Want to play 'Higer or Lower'? Type 'y' to play, hit ENTER to exit: ").lower() == 'y':
    os.system("clear")
    print(logo)
    play_round(pick_account())
  else:
    print("\nGoodbye")

start()