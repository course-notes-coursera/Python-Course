# Comprehensive Exception Handling Examples

# Basic Exception Handling
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

# Handling Multiple Exceptions
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Using else and finally with exceptions
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print("\n--- File Content ---")
        print(content)
except FileNotFoundError:
    print("Error: The file 'example.txt' does not exist.")
else:
    print("File read successfully!")
finally:
    print("End of file operation.")

# Custom Exceptions
class CustomError(Exception):
    """A custom exception for demonstration."""
    pass

try:
    value = int(input("Enter a number greater than 10: "))
    if value <= 10:
        raise CustomError("The number must be greater than 10.")
    print(f"Your number is: {value}")
except CustomError as e:
    print(f"Custom Error: {e}")
except ValueError:
    print("Error: Please enter a valid number.")

# Nested Exception Handling
try:
    try:
        with open('non_existent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Inner Exception: {e}")
        raise  # Re-raise the exception to be handled by the outer block
except Exception as e:
    print(f"Outer Exception: {e}")

# Exception Handling in File Writing
try:
    with open('example_write.txt', 'w') as file:
        file.write("This is some test content written to the file.\n")
        raise IOError("Simulated I/O error while writing.")  # Simulating an error
except IOError as e:
    print(f"Error during file writing: {e}")
finally:
    print("Write operation attempt completed.")

# Catching and handling all exceptions
try:
    # A block with potential errors
    print(10 / 0)  # Will raise ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")

# Using Assertions
try:
    x = int(input("Enter a positive number: "))
    assert x > 0, "Number must be positive."
    print(f"You entered a valid positive number: {x}")
except AssertionError as e:
    print(f"Assertion Error: {e}")

# Raising Exceptions Dynamically
try:
    user_input = input("Enter 'yes' to continue: ").strip().lower()
    if user_input != "yes":
        raise ValueError("Input must be 'yes'.")
    print("You chose to continue!")
except ValueError as e:
    print(f"Error: {e}")

# Multiple Except Blocks and Exception Hierarchy
try:
    lst = [1, 2, 3]
    index = int(input("Enter an index to access: "))
    print(lst[index])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
