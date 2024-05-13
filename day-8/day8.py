import caesar_art as c_art

### PHASE ONE of the caesar cipher, with both an encrypt and decrypt function:

# def encrypt(text, shift):
#   cipher_text = ""
#   for letter in text:
#     cipher_index = alphabet.index(letter) + shift

#     while cipher_index >= len(alphabet):
#       cipher_index -= len(alphabet)

#     cipher_letter = alphabet[cipher_index]
#     cipher_text += cipher_letter
#   print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#   deciphered_text = ""
#   for letter in text:
#     deciphered_index = alphabet.index(letter) - shift

#     while deciphered_index < 0:
#       deciphered_index += len(alphabet)

#     deciphered_letter = alphabet[deciphered_index]
#     deciphered_text += deciphered_letter
#   print(f"The decoded text is {deciphered_text}")

# match direction:
#   case 'encode':
#     encrypt(text=text, shift=shift)
#   case 'decode':
#     decrypt(text=text, shift=shift)

# --------------------------------------- #

### PHASE TWO of the caesar cipher where both encryption and decryption have been consolidated
### and are controlled by the specified direction argument

def caesar(text, shift, direction):    
  if direction == "decode":
    shift = -shift
  
  output = ""
  for char in text:
    if char in alphabet:
      position = alphabet.index(char) + shift
      output += alphabet[position]
    else:
      output += char
  
  print(f"The {direction}d text is {output}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(c_art.logo)

program_running = True

while program_running:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) % len(alphabet)

  caesar(text=text, shift=shift, direction=direction)

  keep_running = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

  if keep_running == "no":
    program_running = False
    print("Goodbye")
