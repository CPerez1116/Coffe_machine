☕ Coffee Machine Simulator (Python)

A simple Python console program that simulates a coffee machine.
Users can order espresso, latte, or cappuccino, insert coins, and receive drinks. 
The program tracks resources (water, milk, coffee) and handles transactions.

This project is a practice project for junior Python developers, focusing on functions, loops, conditionals, and basic resource management.

-----------------------🚀 Features---------------------------------------------

- Choose from espresso, latte, or cappuccino

- Insert coins (quarters, dimes, nickels, pennies)

- Checks if enough ingredients are available before making a drink

- Handles transactions: gives change or refunds if insufficient money

- Prints a report showing remaining resources and money collected

- Allows turning the machine off

-----------------------🛠️ How to Run-----------------------------------

1. Clone the repository:

git clone https://github.com/your-username/coffee-machine.git
cd coffee-machine


2. Run the script with Python 3:

python coffee_machine.py


3. Follow the prompts in the terminal.

----------------------📖 Example Usage-------------------------------------
What would you like? (espresso/latte/cappuccino): latte
Please insert coins
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Total inserted: $2.50
Here is $0.0 dollars in change.
Here is your latte. Enjoy! ☕


Report command:

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 58g
Money: $2.5

      ( (
       ) )
    .-""""-.
   |        |
   |  COFFEE |
   |        |
    `-....-'

----------------📚 What I Learned--------------------------------------

- How to structure code using functions for clarity

- How to use loops and conditionals to control program flow

- Managing resources with dictionaries in Python

- Handling user input and basic error checking

- Importance of writing clear comments and documentation

------------------✨ Future Improvements--------------------------------

- Refactor into a class-based CoffeeMachine object

- Add a GUI version using Tkinter

- Allow the machine to be refilled with resources

- Add more drink options
