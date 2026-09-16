import bank
receiver = 9876543210


def transfer():
    receiver_number = int(input('Enter Account number to transfer Amount: '))
    if receiver_number == receiver:
        amount = int(input('Enter amount to transfer: '))
        if bank.balance >= amount:
            bank.balance -= amount
            return 'Transfer Successful'
        return 'Insufficient'
    else:
        print('Enter correct Receiver Account Number')
        return transfer()
