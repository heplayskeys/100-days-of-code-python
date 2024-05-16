import os
from random import randint
from higher_or_lower_art import logo, versus

DICE = ["🎲", "🎲", "🎲", "🎲"]

def play_round(roll_1, score=0):
  show_dice(roll_1)
  guess = make_guess()
  print(versus)
  roll_2 = roll_dice()
  show_dice(roll_2)

  if guess_correct(sum(roll_1), sum(roll_2), guess):
    score += 1
    input("CORRECT! Press ENTER to keep going...")
    os.system("clear")
    return play_round(roll_2, score)
  else:
    correct_answer = "higher" if guess == "l" else "lower"
    print(f"WRONG! It was {correct_answer}.\nYou scored {score} {'points' if score > 1 else 'point'}.")

  return start()

def roll_dice():
  roll = []
  for _ in DICE:
    value = randint(1, 6)
    roll.append(value)
  return roll

def make_guess():
  return input("Will the next roll be higher or lower? Type 'h' or 'l': ").lower()

def show_dice(roll):
  for i in range(0, len(roll)):
    print(f"{DICE[i]}: {roll[i]}")
  print(f"Total: {sum(roll)}\n")

def guess_correct(roll_1, roll_2, guess):
  if (roll_1 < roll_2) and (guess == "h"):
    return True
  elif (roll_1 > roll_2) and (guess == "l"):
    return True
  return False

def start():
  if input("Want to play 'Higer or Lower'? Type 'y' to play, hit ENTER to exit: ").lower() == 'y':
    os.system("clear")
    print(logo)
    play_round(roll_dice())
  else:
    print("\nGoodbye")

start()