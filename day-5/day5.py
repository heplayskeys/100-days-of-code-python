import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_matrix = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Easy Password - Order not randomized:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""
for _ in range(0, num_letters):
  easy_password += random.choice(letters)

for _ in range(0, num_symbols):
  easy_password += random.choice(symbols)

for _ in range(0, num_numbers):
  easy_password += random.choice(numbers)

# Hard Password - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = ""
total_characters = num_letters + num_symbols + num_numbers
for _ in range(0, total_characters):
  type = random.choice(password_matrix)
  value = random.choice(type)
  hard_password += value

print(f"Here is your easy password: {easy_password}")
print(f"Here is your hard password: {hard_password}")
