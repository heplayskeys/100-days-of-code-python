import os
from random import choice
from higher_or_lower_art import logo, versus
from game_data import data

played = set()

def play_round(account_1, score=0):
  round_accounts = {
    'A': account_1,
  }
  show_info(account_1, 'A')
  print(versus)
  account_2 = pick_account()
  played.add(account_1['name'])

  while account_2['name'] in played:
    account_2 = pick_account()

  played.add(account_2['name'])
  round_accounts['B'] = account_2
  show_info(account_2, 'B')
  guess = make_guess()
  correct_answer = guess_correct(account_1['follower_count'], account_2['follower_count'], guess)

  if correct_answer:
    print("CORRECT!")
    print(f"{round_accounts[guess]['name']} has {round_accounts[guess]['follower_count']} million followers!")
    score += 1

    if len(played) == len(data):
      print("\nYOU DID IT! You guessed them ALL correct! Well done!\n")
      return
    else:
      input("Press ENTER to continue...")
      os.system("clear")
      print(logo)
      return play_round(round_accounts[guess], score)
  else:
    correct_answer = account_2 if guess == "A" else account_1
    print(f"WRONG! It was {correct_answer['name']} with {correct_answer['follower_count']} million followers.")
    print(f"You scored {score} {'points' if score > 1 else 'point'}.")
  return start()

def pick_account():
  return choice(data)

def show_info(account, ltr):
  print(f"Compare {ltr}: {account['name']}, a {account['description']}, from {account['country']}.")

def make_guess():
  return input("Who has more followers? Type 'A' or 'B': ").upper()

def guess_correct(account_1_followers, account_2_followers, guess):
  if (account_1_followers > account_2_followers) and (guess == "A"):
    return True
  elif (account_1_followers < account_2_followers) and (guess == "B"):
    return True
  return False

def start():
  if input("Want to play 'Higer or Lower'? Type 'y' to play, hit ENTER to exit: ").lower() == 'y':
    os.system("clear")
    print(logo)
    play_round(pick_account())
  else:
    print("\nGoodbye")

start()