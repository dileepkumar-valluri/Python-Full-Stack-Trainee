Base = 10000
age = int(input('Enter Age: '))
health_score = int(input('Enter Health Score: '))
Vehical_type = input('Enter Vehical Type: ')

# Checking Age
if age < 25:
    Base *= 1.2
elif age > 50:
    Base *= 1.15

# Checking Health Score

if health_score >= 80:
    Base *= 0.9
elif health_score < 60:
    Base *= 1.2

# Checking Vehical Type

if Vehical_type == 'Sports':
    Base *= 1.3
elif Vehical_type == 'SUV':
    Base *= 1.15
print(f'Final Price is: {round(Base, 2)}')
