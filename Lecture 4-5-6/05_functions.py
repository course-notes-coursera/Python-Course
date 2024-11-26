# Python Functions Explained - Detailed Script

# 1. Defining a Simple Function
# A function in Python is defined using the 'def' keyword, followed by the function name and parentheses.

def greet():
    """This function prints 'Hello, World!'."""
    print("Hello, World!")  # Function body - action performed when function is called

# Calling the 'greet' function. This will execute the code inside the function.
greet()  # Output: Hello, World!

# ------------------------------------------

# 2. Functions with Arguments (Parameters)
# Functions can take inputs in the form of arguments. These arguments are specified inside parentheses when defining the function.

def greet_person(name):
    """This function takes one argument, 'name', and prints a personalized greeting."""
    print(f"Hello, {name}!")  # 'name' is an argument passed to the function

# Calling the function with different arguments.
greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob")    # Output: Hello, Bob!

# ------------------------------------------

# 3. Functions with Multiple Arguments
# Functions can accept multiple arguments. They can then use these arguments in the function body to perform actions.

def add_numbers(num1, num2):
    """This function adds two numbers and prints the result."""
    result = num1 + num2  # Adds the two numbers
    print(f"Sum: {result}")  # Prints the result

# Calling the function with two arguments.
add_numbers(5, 3)  # Output: Sum: 8
add_numbers(10, 20)  # Output: Sum: 30

# ------------------------------------------

# 4. Returning Values from Functions
# Functions can also return values using the 'return' keyword. This allows the caller to store and use the result.

def find_square(num):
    """This function returns the square of a given number."""
    return num * num  # Returns the result (square of the number)

# Calling the function and storing the returned result.
square = find_square(4)
print(f"Square of 4 is {square}")  # Output: Square of 4 is 16

# ------------------------------------------

# 5. The 'pass' Statement
# The 'pass' statement is used as a placeholder for future code. It is often used when defining a function or class that you haven't implemented yet.

def future_function():
    """This function does nothing for now (placeholder)."""
    pass  # No action, just a placeholder

# Calling the function that does nothing.
future_function()  # No output, the function doesn't do anything yet.

# ------------------------------------------

# 6. Using Python's Built-in Functions
# Python provides many built-in functions that we can use directly in our code without defining them ourselves.

import math

# Using the built-in 'sqrt()' function from the math module to calculate the square root of a number.
square_root = math.sqrt(16)  # Calculates the square root of 16
print(f"Square root of 16 is {square_root}")  # Output: Square root of 16 is 4.0

# Using the built-in 'pow()' function to calculate the power of a number.
power = pow(2, 3)  # Calculates 2 raised to the power of 3
print(f"2 to the power of 3 is {power}")  # Output: 2 to the power of 3 is 8

# ------------------------------------------

# 7. Using *args (Variable Number of Positional Arguments)
# The *args syntax allows a function to accept any number of positional arguments, which are passed as a tuple.

def print_numbers(*args):
    """This function prints all the numbers passed as arguments."""
    for number in args:
        print(number)  # Prints each number in the 'args' tuple

# Calling the function with different numbers of arguments.
print_numbers(1, 2, 3, 4)  # Output: 1 2 3 4 (each number printed on a new line)
print_numbers(10, 20)  # Output: 10 20 (each number printed on a new line)

# ------------------------------------------

# 8. Using **kwargs (Variable Number of Keyword Arguments)
# The **kwargs syntax allows a function to accept any number of keyword arguments, which are passed as a dictionary.

def print_person_info(**kwargs):
    """This function prints key-value pairs from the keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")  # Prints each key-value pair from the 'kwargs' dictionary

# Calling the function with keyword arguments.
print_person_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

# ------------------------------------------

# 9. Combining *args and **kwargs
# You can use both *args and **kwargs in the same function. *args must appear before **kwargs.

def display_info(*args, **kwargs):
    """This function accepts both positional and keyword arguments."""
    print("Positional Arguments:", args)  # Prints the tuple of positional arguments
    print("Keyword Arguments:", kwargs)  # Prints the dictionary of keyword arguments

# Calling the function with both positional and keyword arguments.
display_info(1, 2, 3, name="Alice", age=30)
# Output:
# Positional Arguments: (1, 2, 3)
# Keyword Arguments: {'name': 'Alice', 'age': 30}

# ------------------------------------------

# 10. Challenge: Prime Number Checker
# Let's write a function that checks if a given number is prime.

def is_prime(num):
    """This function checks if a number is prime."""
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility from 2 to the square root of num
        if num % i == 0:  # If divisible, the number is not prime
            return False
    return True  # If no divisors are found, the number is prime

# Testing the prime checker function
print(is_prime(13))  # Output: True (13 is prime)
print(is_prime(12))  # Output: False (12 is not prime)

# ------------------------------------------

# 11. Function Documentation with Docstrings
# You can document your functions using docstrings. Docstrings provide a description of the function's purpose.

def multiply(a, b):
    """
    This function takes two numbers as input and returns their product.
    Arguments:
    a -- First number
    b -- Second number
    """
    return a * b  # Returns the product of a and b

# Calling the function
product = multiply(2, 3)
print(f"Product of 2 and 3 is {product}")  # Output: Product of 2 and 3 is 6
