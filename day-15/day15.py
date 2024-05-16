COINS = {
  "quarters": 0.25,
  "dimes": 0.10,
  "nickels": 0.05,
  "pennies": 0.01,
}

MEASUREMENTS = {
  "water": "ml",
  "milk": "ml",
  "coffee": "g",
}

MENU = {
  "espresso": {
    "ingredients": {
        "water": 50,
        "coffee": 18,
    },
    "cost": 1.5,
  },
  "latte": {
    "ingredients": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
    },
    "cost": 2.5,
  },
  "cappuccino": {
    "ingredients": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
    },
    "cost": 3.0,
  }
}

options = [
  *MENU.keys(),
  "report",
  "off"
]

profit = 0

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}


def take_order():
  """Retrieves user input order and processes transaction"""
  order = input("What would you like? (espresso/latte/cappuccino): ").lower()
  if order in options:
    if order in MENU:
      if not sufficient_resources(MENU[order]):
        return take_order()

      if process_coins(MENU[order]["cost"]) > 0:
          add_profit(MENU[order]["cost"])
      else:
          return take_order()

      make_coffee(MENU[order])
      print(dispense(order))
    elif order == "report":
      print_report()
    elif order == "off":
      print("\nThank you! Goodbye.\n")
      return
  else:
    print("Invalid input. Please try again.")

  return take_order()


def sufficient_resources(drink):
  """Checks available resources to make drink and returns if there is enough for the order to be completed"""
  for resource in resources:
    ingredients = drink["ingredients"]
    if resource in ingredients and ingredients[resource] > resources[resource]:
      print(f"Sorry, there is not enough {resource}.")
      if input("Would you like to refill the machine? Type 'y' or 'n': ") == 'y':
        refill_machine()
        print("Machine has been refilled. Processing your order...")
        return True
      else:
        return False
  return True

def process_coins(cost):
  inserted_coins = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0,
  }

  print("Please insert coins.")

  total = 0
  for coin in inserted_coins:
    num_coin = input(f"How many {coin}?: ")
    inserted_coins[coin] = 0 if num_coin == "" else int(num_coin)
    total += COINS[coin] * inserted_coins[coin]

  if total < cost:
    print("Sorry, that's not enough money. Money refunded.\n")
    return 0

  if round(total - cost, 2) > 0.00:
    print(f"Here is ${round(total - cost, 2)} dollars in change.")

  return cost

def make_coffee(drink):
  for ingredient in drink["ingredients"]:
    resources[ingredient] -= drink["ingredients"][ingredient]

def dispense(drink):
  """Takes customer drink order and returns message"""
  return f"Here is your {drink}. Enjoy!\n"

def print_report():
  for resource in resources:
    print(f"{resource.title()}: {resources[resource]}{MEASUREMENTS[resource]}")
  print(f"Money: ${profit}\n")

def add_profit(amount):
  global profit
  profit += amount

def refill_machine():
  global resources
  resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
  }

take_order()
