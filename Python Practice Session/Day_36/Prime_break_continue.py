def Prime_number():
    n = int(input('Enter number: '))
    if n < 100:
        print('Enter N value must be greater than 100')
        Prime_number()
    else:
        for i in range(100, n+1):
            count = 0
            for j in range(1, i+1):
                if i % j == 0:
                    count += 1
            if count == 2:
                print(f'First Prime number after 100 is :{i}')
                break


Prime_number()
