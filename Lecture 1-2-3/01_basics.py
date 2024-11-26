# Python Basics

# Introduction
# Python is an interpreted, high-level, general-purpose programming language.
# It was created by Guido van Rossum and first released in 1991.
# Python is known for its easy-to-read syntax, versatility, and wide range of applications.

# Variables and Data Types
# Variables are containers for storing data values.
# Python is dynamically typed, meaning you don't need to declare the type of a variable.

# Integer Examples
x = 5  # Integer variable
y = -10  # Negative Integer
z = 0  # Zero Integer

# Print integer examples
print(f"x is an integer: {x}")
print(f"y is an integer: {y}")
print(f"z is an integer: {z}")

# Float Examples
pi = 3.14159  # Float variable (Pi)
temperature = 22.5  # Float variable
height = 1.75  # Float variable (in meters)

# Print float examples
print(f"pi is a float: {pi}")
print(f"temperature is a float: {temperature}")
print(f"height is a float: {height}")

# Arithmetic with Integer and Float
a = 10  # Integer
b = 4  # Integer

# Perform arithmetic operations
sum_ab = a + b  # Addition
diff_ab = a - b  # Subtraction
prod_ab = a * b  # Multiplication
quot_ab = a / b  # Division (float result)
int_div_ab = a // b  # Integer division (floor result)
mod_ab = a % b  # Modulus operation (remainder)

# Print results of arithmetic operations
print(f"Sum: {sum_ab}")
print(f"Difference: {diff_ab}")
print(f"Product: {prod_ab}")
print(f"Quotient: {quot_ab}")
print(f"Integer Division: {int_div_ab}")
print(f"Modulus: {mod_ab}")

# String Examples
name = "Alice"  # String variable
greeting = "Hello, " + name + "!"  # Concatenating strings
sentence = f"Welcome, {name}!"  # Using formatted string

# Print string examples
print(f"name is a string: {name}")
print(f"greeting is a string: {greeting}")
print(f"sentence is a string: {sentence}")

# Boolean Examples
is_student = True  # Boolean variable
has_license = False  # Boolean variable

# Print boolean examples
print(f"is_student is a boolean: {is_student}")
print(f"has_license is a boolean: {has_license}")

# Combining booleans in conditions
can_drive = is_student and has_license
print(f"can_drive is: {can_drive}")  # Output: False, as has_license is False

# Modules

# Importing the math module for mathematical operations
import math

# Using functions from math module
square_root = math.sqrt(16)  # Square root of a number
log_value = math.log(100, 10)  # Logarithm (base 10)
power_value = math.pow(2, 3)  # 2 raised to the power of 3

# Print results from math module
print(f"Square root of 16: {square_root}")
print(f"Logarithm of 100 to the base 10: {log_value}")
print(f"2 raised to the power of 3: {power_value}")

# Importing specific function from math module
from math import pi, radians

# Using the imported functions directly
angle_in_degrees = 90
angle_in_radians = radians(angle_in_degrees)  # Convert degrees to radians

# Print results of specific imports
print(f"Value of pi: {pi}")
print(f"Angle {angle_in_degrees} degrees is {angle_in_radians} radians")

# Example of floating point precision and rounding
float_value = 10.56789
rounded_value = round(float_value, 2)  # Round to 2 decimal places
print(f"Rounded value of {float_value} is: {rounded_value}")

#Multi Line and Single Line Comments
# This program demonstrates how to use comments in Python

x = 5  # Assign 5 to variable x
y = 10  # Assign 10 to variable y

# Adding the two numbers
sum_result = x + y

'''
This block calculates the sum of x and y
and prints the result.
It uses the print() function.
'''

print(f"The sum of {x} and {y} is: {sum_result}")
