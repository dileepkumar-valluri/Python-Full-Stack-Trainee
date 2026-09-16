import bank


def attempt():
    new_pin = int(input("Enter New Pin: "))
    second_attempt = int(input('Enter Confirm New PIN: '))
    if new_pin == second_attempt:
        bank.pin = new_pin
        print('Pin Changed')
    else:
        print('Pin doesnt matches')
        attempt()


def Pin_generation():
    PIN = int(input('Enter PIN to proceed: '))
    if bank.pin == PIN:
        attempt()
    else:
        print('Wrong PIN')
        Pin_generation()
