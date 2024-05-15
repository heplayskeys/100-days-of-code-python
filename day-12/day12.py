import os
from random import randint
from guess_the_number_art import logo

EASY_GUESSES = 10
HARD_GUESSES = 5

def new_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

def get_magic_number():
  return randint(1, 100)

def guess():
  return int(input("Make a guess: "))

def check_guess(guess, magic_number, guesses):
  if guess > magic_number:
    print("Too high.")
    return guesses - 1
  elif guess < magic_number:
    print("Too low.")
    return guesses - 1
  else:
    return -1

def play_again():
  if input("\nWould you like to play again? Type 'y' or 'n': ").lower() == 'y':
    return True
  return False

def set_difficulty():
  if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'hard':
    return HARD_GUESSES
  else:
    return EASY_GUESSES

def play():
  new_game()
  magic_number = get_magic_number()
  guesses = set_difficulty()

  while guesses > 0:
    print(f"You have {guesses} attempts remaining to guess the number.")
    guesses = check_guess(guess(), magic_number, guesses)
    if guesses > 0:
      print("Guess again.")

  if guesses == -1:
    print("You got it! You win!")
  else:
    print(f"Sorry. Out of guesses. You lose. The magic number was {magic_number}.")

  if play_again():
    os.system("clear")
    return play()
  
play()