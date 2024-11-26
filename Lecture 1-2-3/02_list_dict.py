# 1. Lists (One-dimensional)
# Lists can store a collection of items, and they are mutable.

# Creating a list (string-based)
fruits = ["apple", "banana", "cherry"]
print("Original Fruits List:", fruits)

# Accessing list items
print(fruits[0])  # apple

# Modifying list items
fruits[1] = "blueberry"
print("Modified Fruits List:", fruits)

# Adding items to the list
fruits.append("orange")
print("Fruits List after append:", fruits)

# Removing items from the list
fruits.remove("cherry")
print("Fruits List after removal:", fruits)

# Looping through a list
print("Looping through fruits list:")
for fruit in fruits:
    print(fruit)

# List Comprehensions (e.g., Squaring numbers)
squares = [x ** 2 for x in range(10)]
print("Squares List (Comprehension):", squares)

# 2. Tuples (Immutable)
# Tuples are similar to lists but cannot be changed once created.

# Creating a tuple (integer-based)
numbers = (1, 2, 3, 4, 5)
print("Original Tuple:", numbers)

# Accessing tuple items
print(numbers[2])  # 3

# Tuples cannot be modified, so no need to modify or remove items.
# You can access and loop through the tuple as shown below:

print("Looping through tuple:")
for number in numbers:
    print(number)

# 3. Arrays (One-dimensional, Integer-based)
# Arrays are like lists but more efficient for numeric data.

import array

# Creating an array of integers
arr = array.array('i', [10, 20, 30, 40, 50])
print("Original Array:", arr)

# Accessing array items
print(arr[2])  # 30

# Modifying array items
arr[1] = 25
print("Modified Array:", arr)

# Adding items to the array
arr.append(60)
print("Array after append:", arr)

# Removing items from the array
arr.remove(30)
print("Array after removal:", arr)

# Looping through an array
print("Looping through array:")
for num in arr:
    print(num)

# 4. Dictionaries (Key-Value pairs)
# Dictionaries store data in key-value pairs, and they are mutable.

# Creating a dictionary (mixed data types: string & integer)
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "is_student": False
}
print("Original Dictionary:", person)

# Accessing dictionary items
print(person["name"])  # Alice

# Modifying dictionary items
person["age"] = 26
print("Modified Dictionary:", person)

# Adding items to the dictionary
person["email"] = "alice@example.com"
print("Dictionary after adding email:", person)

# Removing items from the dictionary
del person["city"]
print("Dictionary after removal of city:", person)

# Looping through a dictionary (key-value pairs)
print("Looping through dictionary items:")
for key, value in person.items():
    print(f"{key}: {value}")

# 5. Lists (Two-dimensional)
# Two-dimensional lists are essentially lists of lists, which can be used to represent matrices.

# Creating a two-dimensional list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Two-dimensional List (Matrix):", matrix)

# Accessing elements in a two-dimensional list
print("Element at position (1,2):", matrix[1][2])  # 6

# Looping through a two-dimensional list
print("Looping through matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # new line after each row

# 6. Arrays (Two-dimensional)
# You can also create two-dimensional arrays using the `array` module, but it's less common.

# Creating a 2D array using the array module
arr2d = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2d = [arr2d[i:i+3] for i in range(0, len(arr2d), 3)]
print("Two-dimensional Array:", arr2d)

# 7. Strings (String-based lists and manipulation)

# Creating a string
message = "Hello, World!"
print("Original String:", message)

# Slicing strings (works like lists)
print(message[0:5])  # "Hello"

# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name
print("Concatenated String:", full_greeting)

# Looping through a string
print("Looping through the string:")
for char in message:
    print(char)

# String formatting (f-strings)
age = 25
formatted_message = f"Hello, my name is {name} and I am {age} years old."
print("Formatted String:", formatted_message)

# 8. Integer-based operations on lists, tuples, and arrays

# Using lists for numeric operations
num_list = [1, 2, 3, 4, 5]
sum_list = sum(num_list)
print("Sum of list:", sum_list)

# Using a tuple for numeric operations (immutable)
num_tuple = (10, 20, 30)
max_tuple = max(num_tuple)
print("Max of tuple:", max_tuple)

# Using arrays for numeric operations
num_array = array.array('i', [10, 20, 30, 40, 50])
avg_array = sum(num_array) / len(num_array)
print("Average of array:", avg_array)
