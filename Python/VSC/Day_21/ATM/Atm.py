import bank
import Transfer
import PIN_generation


def ATM():
    while True:
        print('1.Check balance')
        print('2.Withdraw')
        print('3.Deposit')
        print('4.Transfer')
        print('5.PIN Genereation')
        print('6.Exit')
        choice = int(input('Select Option: '))
        if choice == 1:
            print('Balance: ', bank.check_balance())
        elif choice == 2:
            result = bank.withdraw()
            if result == 'Insuffient funds':
                print(result)
            else:
                print('Withdraw Succesfull and Your Balance is: ', result)
        elif choice == 3:
            print('Deposit Successful and Your Balance is: ', bank.deposit())
        elif choice == 4:
            print(Transfer.transfer())
        elif choice == 5:
            PIN_generation.Pin_generation()
        elif choice == 6:
            exit()

        else:
            print('Invalid Choice')


card = input('Insert Your Card: ').lower()
if card == 'yes':
    print('Card Inserted Successfully')
    while True:
        if bank.pin_verification() == 'Correct pin':
            ATM()
        else:
            print('Incorrect Pin')
            print('1.Try Again')
            print('2.Exit')
            pc = int(input('Select Option: '))
            if pc == 1:
                continue
            elif pc == 2:
                exit()
            else:
                print('Invalid Option')
elif card == 'no':
    print('Please Insert your Card Properly')
else:
    exit()
