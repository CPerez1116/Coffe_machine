# Coffee Machine Program
# ----------------------
# This simulates a coffee machine where the user can buy espresso, latte, or cappuccino.
# It tracks resources (water, milk, coffee), processes coin inputs, and handles transactions.

# Menu with ingredients and costs for each drink
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

# Starting money inside the machine
money = 0

# Machine resources (like an inventory)
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Function to check if enough ingredients are available
def check_resources(ingredients_4_drinks):
    # Loop through each required ingredient
    for item in ingredients_4_drinks:
        # If any ingredient needed is more than what we have, we cannot make the drink
        if ingredients_4_drinks[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Function to ask the user for coins and calculate total amount inserted
def process_coins():
    print("Please insert coins")
    # Convert the input to float so we can multiply by coin values
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    # Total money is the sum of all coins inserted
    total_money_inserted = round(
        (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2
    )
    print(f"Total inserted: ${total_money_inserted}")
    return total_money_inserted


# Function to check if transaction was successful
def transaction_success(coins_inserted, cost):
    if coins_inserted >= cost:
        # Calculate change if user inserted more than required
        change = round(coins_inserted - cost, 2)
        print(f"Here is ${change} dollars in change.")

        # Update global money inside the machine
        global money
        money += cost
        return True
    else:
        # If not enough money, refund
        print("Sorry that's not enough money. Money refunded.")
        return False


# Function to actually make the coffee and update resources
def make_coffee(drink_name, ingredients):
    # Subtract used resources from the machine inventory
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


# Main program loop
while True:
    # Ask user for their choice
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        # Stop the program when 'off' is typed
        print("Goodbye!")
        break
    elif choice == "report":
        # Print current resources and money in machine
        print(f"Water: {resources['water']}ml"
              f"\nMilk: {resources['milk']}ml"
              f"\nCoffee: {resources['coffee']}g"
              f"\nMoney: ${money}")
    elif choice in MENU:
        # Step 1: Check if enough ingredients
        if check_resources(MENU[choice]["ingredients"]):
            # Step 2: Ask user to insert coins
            currency = process_coins()
            # Step 3: Check if enough money was inserted
            if transaction_success(currency, MENU[choice]["cost"]):
                # Step 4: Make the coffee
                make_coffee(choice, MENU[choice]["ingredients"])
    else:
        print("Option not available, please select again!")
