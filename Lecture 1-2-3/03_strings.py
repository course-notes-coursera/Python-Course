# Strings in Python: Comprehensive Guide

# 1. Creating Strings
single_quote_str = 'Hello'
double_quote_str = "World"
triple_quote_str = '''This is a
multiline string.'''

# Display the created strings
print("Single quote string:", single_quote_str)
print("Double quote string:", double_quote_str)
print("Triple quote string:", triple_quote_str)

# 2. String Concatenation
str1 = "Hello"
str2 = "World"
greeting = str1 + " " + str2  # Concatenating strings with a space
print("Concatenated string:", greeting)

# 3. String Length
length = len(greeting)  # Length of the greeting string
print("Length of greeting:", length)

# 4. Accessing Characters
first_char = greeting[0]  # First character
last_char = greeting[-1]  # Last character
print(f"First character: {first_char}, Last character: {last_char}")

# 5. Slicing Strings
substring = greeting[0:5]  # Slicing to get "Hello"
print("Substring (0:5):", substring)

# 6. String Methods

# Convert to uppercase and lowercase
upper_str = greeting.upper()  # "HELLO WORLD"
lower_str = greeting.lower()  # "hello world"
print("Uppercase:", upper_str)
print("Lowercase:", lower_str)

# Stripping whitespaces
whitespace_str = "   Hello, World!   "
stripped_str = whitespace_str.strip()  # Removes leading/trailing spaces
print(f"Stripped string: '{stripped_str}'")

# Replacing a substring
replaced_str = greeting.replace("World", "Python")  # "Hello Python"
print("Replaced string:", replaced_str)

# Splitting and joining strings
split_str = greeting.split(" ")  # Splitting at space results in ['Hello', 'World']
print("Split string:", split_str)
joined_str = " ".join(split_str)  # Joining back with space
print("Joined string:", joined_str)

# Find and rfind (First and Last occurrence)
index_of_World = greeting.find("World")  # Finds first occurrence of "World"
index_of_last_o = greeting.rfind("o")  # Finds last occurrence of "o"
print(f"Index of 'World': {index_of_World}, Index of last 'o': {index_of_last_o}")

# Check if string starts/ends with certain substrings
starts_with_Hello = greeting.startswith("Hello")  # True
ends_with_exclamation = greeting.endswith("!")  # False
print(f"Starts with 'Hello': {starts_with_Hello}, Ends with '!': {ends_with_exclamation}")

# 7. String Formatting

# %-formatting
name = "Alice"
age = 25
formatted_str = "My name is %s and I am %d years old." % (name, age)
print("Formatted with %:", formatted_str)

# str.format() method
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print("Formatted with .format():", formatted_str)

# f-strings (Python 3.6+)
formatted_str = f"My name is {name} and I am {age} years old."
print("Formatted with f-strings:", formatted_str)

# 8. Escape Characters
newline_str = "Hello\nWorld!"  # Newline
tabbed_str = "Hello\tWorld!"  # Tab
escaped_quote_str = "He said, \"Hello, World!\""  # Escaped quotes
print("Newline string:", newline_str)
print("Tabbed string:", tabbed_str)
print("Escaped quote string:", escaped_quote_str)

# 9. String Interpolation
expression_str = f"The sum of 2 and 3 is {2 + 3}."  # Directly inserting expressions
print(expression_str)

# 10. Multiline Strings
multiline_str = """This is a string
that spans multiple
lines."""
print("Multiline string:")
print(multiline_str)

# 11. Raw Strings (Useful for file paths and regular expressions)
raw_str = r"C:\Users\Alice\Documents"  # Backslashes treated literally
print("Raw string:", raw_str)

# 12. String Testing Methods

# isalpha() - checks if all characters are alphabetic
print("Is 'Hello' alphabetic?", "Hello".isalpha())  # True
# isdigit() - checks if all characters are digits
print("Is '12345' a digit?", "12345".isdigit())  # True
# isalnum() - checks if all characters are alphanumeric
print("Is 'Hello123' alphanumeric?", "Hello123".isalnum())  # True
# isspace() - checks if all characters are whitespace
print("Is '   ' whitespace?", "   ".isspace())  # True

# isupper() and islower() - checks case
print("Is 'HELLO' uppercase?", "HELLO".isupper())  # True
print("Is 'hello' lowercase?", "hello".islower())  # True

# istitle() - checks if the string is in title case
print("Is 'Hello World' in title case?", "Hello World".istitle())  # True

# 13. String Comparison
str1 = "apple"
str2 = "banana"
print(f"Is 'apple' less than 'banana'?", str1 < str2)  # True (lexicographical comparison)

# 14. Unicode and Encoding
unicode_str = "Hello"
encoded_str = unicode_str.encode('utf-8')  # Encodes to bytes
print(f"Encoded string (utf-8): {encoded_str}")

decoded_str = encoded_str.decode('utf-8')  # Decodes back to string
print(f"Decoded string: {decoded_str}")

# 15. String Alignment Methods
text = "Hello"
print(f"Center-aligned: '{text.center(10)}'")
print(f"Left-justified: '{text.ljust(10, '*')}'")
print(f"Right-justified: '{text.rjust(10, '*')}'")
print(f"Zero-padded: '{text.zfill(10)}'")

# 16. Working with String Case Conversion Methods
text = "hello"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Title case: {text.title()}")

# Final Summary
print("\nSummary:")
print(f"String manipulation methods demonstrated successfully. The string '{greeting}' has been transformed and tested using various string methods such as concatenation, case conversion, slicing, formatting, and testing properties (e.g., isalpha, isdigit).")

