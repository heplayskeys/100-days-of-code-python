import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
player_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if player_choice not in [0, 1, 2]:
  print("Invalid entry. You lose.")
  exit()

computer_choice = random.randint(0, 2)

print(choices[player_choice])
print("Computer chose:")
print(choices[computer_choice])

outcome = player_choice - computer_choice

if outcome == 1 or outcome == -2:
  print("You win!")
elif outcome == 0:
  print("It's a tie!")
else:
  print("You lose!")