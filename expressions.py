# String Manipulation Program
# Asking the user for their first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenating the first name and last name to get the full name
full_name = first_name + " " + last_name

# Printing the greeting message with the full name
print("Hello, " + full_name + "! Welcome!")

# Arithmetic Operations Program
# Asking the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
integer_div_result = int(num1 // num2)  # Integer division
float_div_result = num1 / num2  # Float division

# Displaying the results
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The difference between {num1} and {num2} is: {difference_result}")
print(f"The product of {num1} and {num2} is: {product_result}")
print(f"The integer division of {num1} by {num2} gives: {integer_div_result}")
print(f"The float division of {num1} by {num2} gives: {float_div_result}")

# Using Functions and Modules Program
import math  # Importing the math module to use pi

# Asking the user to input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculating the area of the circle using the formula: Area = π * r²
area = math.pi * (radius ** 2)

# Displaying the result with a message
print(f"The area of the circle with radius {radius} is: {area:.2f}")


