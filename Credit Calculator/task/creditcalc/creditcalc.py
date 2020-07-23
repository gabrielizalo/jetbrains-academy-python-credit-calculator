import math

# Globals
credit_main = 0
calculate_type = None


# Functions
def begin():
    global credit_main
    global calculate_type

    print('Enter the credit principal:')
    credit_main = int(input())

    print('What do you want to calculate?')
    print('type "m" - for count of months,')
    print('type "p" - for monthly payment:')
    while calculate_type != 'm' and calculate_type != 'p':
        calculate_type = input()


def calculate_months():
    global credit_main
    print('Enter monthly payment:')
    payment = int(input())
    months = int(credit_main / payment)
    if credit_main % payment > 0:
        months += 1
    print(f'It takes {months} to repay the credit')


def calculate_payment():
    global credit_main
    print('Enter count of months:')
    months = int(input())
    payment = math.ceil(credit_main / months)
    str_payment = f'Your monthly payment = {payment}'
    if payment * months != credit_main:
        difference = payment + (credit_main - (payment * months))
        str_payment += f' with last month payment = {difference}.'
    print(str_payment)


# Main
begin()
if calculate_type == 'm':
    calculate_months()
else:
    calculate_payment()
