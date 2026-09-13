import Addition
import Subtraction
import Multiplication
import Division


def Operation():
    choose = input('Select Mathematical Operation from +,-,*,/: ')
    if choose == '+':
        a = map(int, input('Enter Numbers to add: ').split())
        print(Addition.addition(a))
    elif choose == '-':
        s = map(int, input('Enter Numbers to Subtract: ').split())
        print(Subtraction.subtraction(s))
    elif choose == '*':
        m = map(int, input('Enter Numbers to Multiply: ').split())
        print(Multiplication.Multiplication(m))
    elif choose == '/':
        print(Division.Division_Operation())
    else:
        print('Choose Correct Operation:')
        return Operation()
    choose_again = input('Select Yes or no to Continue: ').lower()
    if choose_again == 'yes':
        return Operation()
    elif choose_again == 'no':
        print('Bye!')
        return
    else:
        print('Invalid! Select Yes or no')
        return Operation()


Operation()
