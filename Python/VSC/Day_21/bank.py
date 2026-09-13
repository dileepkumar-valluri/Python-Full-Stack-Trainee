balance = 1000


def deposit(amount):
    global balance
    return balance+amount


def withdraw(amount):
    global balance
    if amount < balance:
        balance -= amount
        return balance
    return 'Insuffient funds'
