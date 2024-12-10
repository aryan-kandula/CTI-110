# Aryan Kandula
# 11/26/2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules
#
# PSEUDOCODE:
# START
# Display user to Enter grades for six modules
# get grade for module 1
# get grade for module 2
# get grade for module 3
# get grade for module 4
# get grade for module 5
# get grade for module 6
# take all grades in list named "grades"
# find lowest of the grades from the list "grades" (low)
# find highest of the grades from the list "grades" (high)
# calculate sum of list "grades" (total)
# calculate average of list "grades" by dividing sum of grades by number of grades(avg)
# print lowest grade
# print highest grade
# print sum of grades
# print average of grades rounded to two decimals
# determining letter grade based on average: 
# If the average is greater than or equal to 90, print "Your grade is: A".
# If the average is greater than or equal to 80, print "Your grade is: B".
# If the average is greater than or equal to 70, print "Your grade is: C".
# If the average is greater than or equal to 60, print "Your grade is: D".
# If the average is less than 60, print "Your grade is: F".
#END


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


grades = [mod_1, mod_2, mod_3, mod_4, mod_5]


low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades) / len(grades)


print ('\n------------Results------------')
print (f'{"Lowest Grade: ":<20}{low}')
print (f'{"Highest Grade: ":<20}{high}')
print (f'{"Sum of Grades: ":<20}{total}')
print (f'{"Average: ":<20}{avg:.2f}\n')

print ('-------------------------------')
if avg >= 90:
    print ('Your grade is: A')
elif avg >= 80:
    print ('Your grade is: B')
elif avg >= 70:
    print ('Your grade is C')
elif avg >= 60:
    print ('Your grade is D')
elif avg >= 0:
    print ('Your grade is F')
else:
    print ('Your grade input is invalid')





