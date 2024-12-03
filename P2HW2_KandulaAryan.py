# Aryan Kandula
# 11/29/2024
# P2HW2
# This program calculates and displays statistics for grades entered by the user.

# Pseudocode:
# Prompt the user to enter grades for Modules 1 to 6.
# Assign each grade input to a separate variable (mod1 to mod6).
# Store these variables in a list named 'grades'.
# Calculate the following:
# - Lowest grade in the list
# - Highest grade in the list
# - Sum of all grades
# - Average of the grades
# Display the results in a formatted manner with specified spacing and two decimal points for the average.

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

grades = [mod1, mod2, mod3, mod4, mod5, mod6]

lowest_grade = min(grades)
highest_grade = max(grades)
grades_sum = sum(grades)
average_grade = grades_sum / len(grades)

print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<20}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<20}{grades_sum:.1f}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("---------------------------------")
