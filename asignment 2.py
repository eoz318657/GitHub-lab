# Prompt the user for their first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate the first name and last name to form the full name
full_name = first_name + " " + last_name

# Print a greeting message including the user's full name
print("Hello, " + full_name + "! Welcome to Python programming.")

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
integer_division = num1 // num2
floating_point_division = num1 / num2

# Display the results
print("\nResults:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Integer Division: {num1} // {num2} = {integer_division}")
print(f"Floating-point Division: {num1} / {num2} = {floating_point_division}")

import math

# Ask the user to input a number
number = float(input("Enter a number to find its square root: "))

# Calculate the square root using math.sqrt()
square_root = math.sqrt(number)

# Print the result
print(f"The square root of {number} is {square_root}")