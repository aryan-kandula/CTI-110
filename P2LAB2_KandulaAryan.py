# Aryan Kandula
# 11/21/2024
# P2LAB2
# Creating Dictionary of vehicles and displaying their MPG
vehicle_mpg = {
    "camaro": 18.21,
    "prius": 52.36,
    "model s": 110,
    "silverado": 26
}
keys = vehicle_mpg.keys()
print(f"Available vehicles: {keys}")
vehicle = input("Enter a vehicle to see its MPG: ")
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"The {vehicle} gets {mpg} MPG.")
    try:
        miles = float(input(f"How many miles will you drive the {vehicle}? "))

        gallons_needed = miles / mpg

        print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
    except ValueError:
        print("Please enter a valid number for miles.")
else:
    print("Vehicle not found. Please ensure the name is entered exactly as shown.")
