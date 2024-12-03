# Aryan Kandula
# 12/03/2024
# P2HW1_TravelExpenses
# This program calculates and displays travel expenses with formatted output.

print("This program calculates and displays travel expenses")
print("")
budget = float(input("Enter Budget: "))
print("")
destination = input("Enter your travel destination: ")
print("")
gas_expense = float(input("How much do you think you will spend on gas? "))
print("")
hotel_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
print("")
food_expense = float(input("Last, how much do you need for food? "))

remaining_balance = budget - (gas_expense + hotel_expense + food_expense)

print("\n----------------Travel Expenses----------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas_expense:,.2f}")
print(f"{'Accommodation:':<20}${hotel_expense:,.2f}")
print(f"{'Food:':<20}${food_expense:,.2f}")
print("---------------------------------------------------\n")
print(f"{'Remaining Balance:':<20}${remaining_balance:,.2f}")