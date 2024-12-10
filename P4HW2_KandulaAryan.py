# Aryan Kandula
# 12/10//24
# P4HW2
# Request employee's name, hours worked, and pay rate
# Put a while loop to let user continue to put information or terminate the program
# Check if hours worked are greater than 40
# If yes, calculate overtime hours and overtime pay
# Calculate regular pay and gross pay including overtime pay
# Else, calculate regular pay and gross pay without overtime
# Display the employee's information and pay details


#request employee information
name = input("Enter employee's name or \"Done\": ")
total_employees = 0
total_overtimePay = 0.0
total_regPay = 0.0
total_grossPay = 0.0

while name != "Done" :
  total_employees += 1
  hoursWorked = float(input("Enter number of hours worked by " + name + ": "))
  payRate = float(input("Enter " + name + "'s pay rate: "))

#calculate overtime
  if hoursWorked > 40:
      overtimeHours = hoursWorked - 40
      overtimePayRate = payRate * 1.5
      overtimePay = overtimeHours * overtimePayRate
      total_overtimePay += overtimePay
      regPay = payRate * (hoursWorked - overtimeHours)
      total_regPay += regPay
      grossPay = regPay + overtimePay
      total_grossPay += grossPay
    
  else:
      overtimeHours = 0
      overtimePay = 0
      total_overtimePay += overtimePay
      regPay = payRate * hoursWorked
      total_regPay += regPay
      grossPay = regPay
      total_grossPay += regPay

#display output
  print("--------------------------------------------------")
  print("Employee name: ", name, "\n")
  print(f'{"Hours Worked":<15}{"Pay Rate":<15}{"OverTime":<15}{"OverTime Pay":<17}{"RegHour Pay":<15}{"Gross Pay":<15}')
  print("--------------------------------------------------------------------------------------------")
  print(f'{hoursWorked:<15.1f}{payRate:<15.2f}{overtimeHours:<15.1f}${overtimePay:<17.2f}${regPay:<15.2f}${grossPay:<15.2f}\n')
  name = input("Enter employee's name or \"Done\" to terminate: ")

print("\nTotal amount of employees entered: " ,total_employees)
print("Total amount paid for overtime: $" ,format(total_overtimePay,".2f"))
print("Total amount paid for regular hours: $" ,format(total_regPay,".2f"))
print("Total amount paid in gross: $" ,format(total_grossPay,".2f"))

