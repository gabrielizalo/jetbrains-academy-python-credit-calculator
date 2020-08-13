import math

# Globals
credit_main = 0
calculate_type = None


# Functions
def begin():
    global calculate_type

    print('What do you want to calculate?')
    print('type "n" - for count of months,')
    print('type "a" - for the annuity monthly payment:')
    print('type "p" - for the credit principal:')
    while calculate_type != 'n' and calculate_type != 'a' and calculate_type != 'p':
        calculate_type = input()


def calculate_months():
    global credit_main

    # User data
    print('Enter the credit principal:')
    credit_main = int(input())
    print('Enter monthly payment:')
    payment = int(input())
    print('Enter the credit interest:')
    interest = int(input())

    # Calculations
    nominal_interest = (interest / 100) / 12
    months = math.log((payment / (payment - nominal_interest * credit_main)), 1 + nominal_interest)
    months = math.ceil(months)

    # Friendly message
    years_user = ''
    months_user = ''
    years = math.floor(months / 12)
    months = months % 12

    if years > 1:
        years_user = f'{years} years'
    elif years > 0:
        years_user = f'{years} year'
    if months > 1:
        months_user = f'{months} months'
    elif months > 0:
        years_user = f'{months} month'

    if len(years_user) > 0 and len(months_user):
        time = f'{years_user} and {months_user}'
    elif len(years_user) > 0:
        time = f'{years_user}'
    else:
        time = f'{months_user}'

    # Finally
    print(f'You need {time} to repay this credit!')


def calculate_payment():
    global credit_main
    print('Enter the credit principal:')
    credit_main = int(input())
    print('Enter count of months:')
    months = int(input())
    payment = math.ceil(credit_main / months)
    str_payment = f'Your monthly payment = {payment}'
    if payment * months != credit_main:
        difference = payment + (credit_main - (payment * months))
        str_payment += f' with last month payment = {difference}.'
    print(str_payment)


def calculate_principal():
    print('Hello')


# Main
begin()
if calculate_type == 'n':
    calculate_months()
elif calculate_type == 'a':
    calculate_payment()
else:
    calculate_principal()
