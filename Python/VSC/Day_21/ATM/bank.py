balance = 1000
pin = 2005


def pin_verification():
    user_pin = int(input('Enter You Pin: '))
    if user_pin == pin:
        return 'Correct pin'
    return 'Incorrect Pin'


def deposit():
    amount = int(input('Enter amount to deposit: '))
    global balance
    balance += amount
    return balance


def withdraw():
    amount = int(input('Enter amount to withdraw: '))
    global balance
    if amount <= balance:
        balance -= amount
        return balance
    return 'Insuffient funds'


def check_balance():
    return balance
