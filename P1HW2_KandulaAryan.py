# Aryan Kandula
# 11/14/2024
# P1HW2
# This program calculates and displays travel expenses

print('This program calculates and displays travel expenses. ')
print()
budget = float(input('Enter Budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gas_cost = float(input('How much do you think you will spend on gas? '))
print()
accomodation_cost = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food_cost = float(input('Last, how much do you need for food? '))
    
total_expenses = gas_cost + accomodation_cost + food_cost
remaining_balance = budget - total_expenses
    
print('\n------------Travel Expenses------------')
print('Location:', destination)
print('Initial Budget:', budget)
print('\nFuel:', gas_cost)
print('Accomodation:', accomodation_cost)
print('Food:', food_cost)
print('------------------------------------------')
print('\nRemaining Balance:', remaining_balance)
