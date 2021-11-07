# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# food = budget.Category("Food")
# entertainment = budget.Category("Entertainment")
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# transfer_amount = 20
# food_balance_before = food.get_balance()
# entertainment_balance_before = entertainment.get_balance()
# good_transfer = food.transfer(transfer_amount, entertainment)
# food_balance_after = food.get_balance()
# entertainment_balance_after = entertainment.get_balance()

# food = budget.Category("Food")
# entertainment = budget.Category("Entertainment")
# business = budget.Category("Business")
#
# food.deposit(900, "deposit")
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)

# print(food)
# print(clothing)
print(create_spend_chart([food, clothing, auto]))
# print(create_spend_chart([food, entertainment, business]))

# Run unit tests automatically
main(module='test_module', exit=False)
