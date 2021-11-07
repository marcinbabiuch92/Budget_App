class Category(object):

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=None):
        self.amount = amount
        if description is None:
            self.description = ''
        else:
            self.description = str(description).strip()
        self.ledger.append({"amount": self.amount, "description": self.description})

    def withdraw(self, amount, description=None):
        self.amount = -amount
        if description is None:
            self.description = ''
        else:
            self.description = str(description).strip()
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": self.amount, "description": self.description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for amount in self.ledger:
            balance += amount['amount']
        return balance

    def transfer(self, amount, category):
        description_withdraw = "Transfer to " + category.name
        description_deposit = "Transfer from " + self.name
        if self.check_funds(amount) is True:
            self.withdraw(amount, description_withdraw)
            category.deposit(amount, description_deposit)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() - amount >= 0:
            return True
        else:
            return False

    def __str__(self):
        expenses = str(self.name).center(30, '*') + '\n'
        total = 0

        for item in self.ledger:
            line = str(item['description'])[0:23].ljust(23) + str(format(item['amount'], '.2f')).rjust(7) + '\n'
            expenses += line
            total += item['amount']

        expenses += "Total: " + str(format(total, '.2f'))

        return expenses

def create_spend_chart(categories):
    percentage = 100
    percentage_money_spent_list = []
    money_spent_list = []
    money_spent_all = 0
    categories_name = []
    chart = "Percentage spent by category"

    for category in categories:
        categories_name.append(category.name)
        money_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                money_spent += -item['amount']
        money_spent_list.append(money_spent)
        money_spent_all += round(money_spent, 2)

    for item in money_spent_list:
        percentage_money_spent_list.append(item/money_spent_all * 100 - (item//money_spent_all) % 10)

    filler = ['   '] * len(categories)

    for line in range(11):
        chart += '\n' + str(percentage).rjust(3) + "|"
        for value in range(len(categories)):
            if percentage <= percentage_money_spent_list[value]:
                filler[value] = ' o '
            chart += str(filler[value])
        chart += ' '
        percentage -= 10

    chart += '\n' + 4*' ' + len(categories)*'---' + '-'
    for category in range(len(max(categories_name, key=len))):
        chart += '\n    '
        for each in range(len(categories)):
            try:
                letter = categories_name[each][category]
            except:
                letter = ' '
            chart += ' ' + letter + ' '
        chart += ' '

    return chart