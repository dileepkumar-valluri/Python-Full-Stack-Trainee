# seat_type = input(
#     'Enter Seat type from Business Seat/Premium Economy/Economy: ')
# booking_days = int(input())
# festival = input('Booking seasion is True/False: ')
# age = int(input())
# Base_Price = 5000
# Total_Price = 0

# # Checking Seat Type
# if seat_type == 'Business Seat':
#     BS = Base_Price*0.4
#     Total_Price = BS+Base_Price
# elif seat_type == 'Premium Economy':
#     PE = Base_Price*0.2
#     Total_Price = PE+Base_Price
# elif seat_type == 'Economy':
#     Total_Price = Base_Price
# else:
#     print('Select Correct Seat Type')

# # Checking Booking Days
# if booking_days > 30:
#     Discount = Total_Price*0.1
#     Total_Price = Total_Price-Discount
# elif booking_days < 7:
#     Increement = Total_Price*0.25
#     Total_Price += Increement

# # Checking Festival or not
# if festival == 'True':
#     festival_price = Total_Price*0.2
#     Total_Price += festival_price

# # Checking Age Eligible
# if age > 60:
#     age_discount = Total_Price*0.15
#     Total_Price = Total_Price-age_discount

# print(f'Final Ticket Price is: {Total_Price}')


seat = input('Enter Your Seat Type: ')
days = int(input('Enter your Booking Days:'))
festival = input('Enter Festival or Not: ').lower() == 'true'
age = int(input('Enter Your age: '))
price = 5000
# Checking Seat Type

if seat == 'Business':
    price *= 1.4
elif seat == 'Premium':
    price *= 1.2

# Checking days

if days > 30:
    price *= 0.9
elif days < 7:
    price *= 1.25

# Checking Festival

if festival:
    price *= 1.2

# Checking Age

if age > 60:
    price *= 0.85

print(price)
