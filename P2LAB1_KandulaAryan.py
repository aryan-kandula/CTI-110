# Aryan Kandula
# 11/26/2024
# CTI 110 2001
# P2LAB1
# Calculating Area and Circumference of Circle
# START
# Introduce variable radius, diameter, circumference, area
# Display What is the radius of the Circle?
# Take input radius
# Set diameter = radius * 2
# Set circumference = 2 * π * radius
# Set area = π * (radius)^2
# Display The Diameter of the circle is ,diameter
# Display The circumference of the circle is ,circumference
# Display The area of the circle is ,area
# END

import math
radius = float(input('What is the radius of the circle? '))
diameter = radius * 2
circumference = 2 * math.pi * radius
area = math.pi * pow(radius,2)
print('\nThe Diameter of the circle is ' ,diameter)
print('\nThe circumference of the circle is ' ,f"{circumference:.2f}")
print('\nThe area of the circle is ' ,f"{area:.3f}")