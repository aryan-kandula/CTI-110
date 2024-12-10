# Aryan Kandula
# 12/03//24
# P3HW2
# Request employee's name, hours worked, and pay rate
# Check if hours worked are greater than 40
# If yes, calculate overtime hours and overtime pay
# Calculate regular pay and gross pay including overtime pay
# Else, calculate regular pay and gross pay without overtime
# Display the employee's information and pay details


#request employee information
name = input("Enter employee's name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

#calculate overtime
if hoursWorked > 40:
    overtimeHours = hoursWorked - 40
    overtimePayRate = payRate * 1.5
    overtimePay = overtimeHours * overtimePayRate
    
    regPay = payRate * (hoursWorked - overtimeHours)
    grossPay = regPay + overtimePay
    
else:
    overtimeHours = 0
    overtimePay = 0
    regPay = payRate * hoursWorked
    grossPay = regPay

#display output
print("--------------------------------------------------")
print("Employee name: ", name, "\n")
print(f'{"Hours Worked":<15}{"Pay Rate":<15}{"OverTime":<15}{"OverTime Pay":<17}{"RegHour Pay":<15}{"Gross Pay":<15}')
print("--------------------------------------------------------------------------------------------")
print(f'{hoursWorked:<15.1f}{payRate:<15}{overtimeHours:<15.1f}${overtimePay:<17.2f}${regPay:<15.2f}${grossPay:<15.2f}')
