from calculator_art import logo
import os

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

CALCULATE = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculate():
  print(logo)

  output = 0
  running = True
  num1 = float(input("\nWhat's the first number?: "))

  while running:
    for operator in CALCULATE:
      print(operator)

    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    output = CALCULATE[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {output}")
    calculate_more = input(f"Type 'y' to continue calculating with {output}, type 'n' to start a new calculation, hit 'enter' to exit: ")
    
    if calculate_more == 'n':
      os.system("clear")
      return calculate()
    elif calculate_more == 'y':
      num1 = output
      print(f"\nThe first number is: {output}")
    else:
      print("\nGoodbye")
      running = False

calculate()