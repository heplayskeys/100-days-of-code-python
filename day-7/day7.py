import random
import hangman_art as h_art
import hangman_words as h_words

chosen_word = random.choice(h_words.word_list)
display = [*("_" * len(chosen_word))]
lives = len(h_art.stages) - 1
letters_guessed = []

print(h_art.logo)
print(h_art.stages[lives])

while "_" in display and lives > 0:
  print(f"{' '.join(display)}\n")
  
  guess = input("Guess a letter: ").lower()

  if guess in letters_guessed:
    print(f"'{guess}' was already guessed. Try again.")
  elif guess in chosen_word:
    for idx, letter in enumerate(chosen_word):
      if letter == guess:
        display[idx] = letter
  else:
    print(f"'{guess}' is not in the word. You lose a life.")
    lives -= 1

  letters_guessed.append(guess)
  print(h_art.stages[lives])

print("You win!") if lives else print("You Lose!")
