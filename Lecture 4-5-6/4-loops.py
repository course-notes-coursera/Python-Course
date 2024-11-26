# 1. FOR LOOP - Iterating over different sequences

# Iterating through a list
numbers = [1, 2, 3, 4, 5]
print("For loop - Iterating through a list:")
for num in numbers:
    print(f"Current number: {num}")

# Iterating through a string
word = "Python"
print("\nFor loop - Iterating through a string:")
for char in word:
    print(f"Character: {char}")

# Using range to iterate a specific number of times
print("\nFor loop - Using range to iterate:")
for i in range(1, 6):  # Iterates from 1 to 5
    print(f"Number from range: {i}")

# 2. WHILE LOOP - Basic while loop with condition

count = 0
print("\nWhile loop - Basic while loop:")
while count < 3:
    print(f"Count is: {count}")
    count += 1

# 3. BREAK - Breaking out of a loop

print("\nWhile loop - Using break to exit early:")
count = 0
while count < 5:
    if count == 3:
        print("Breaking the loop at count = 3.")
        break
    print(f"Count: {count}")
    count += 1

# 4. CONTINUE - Skipping an iteration

print("\nWhile loop - Using continue to skip an iteration:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping count = 3")
        continue
    print(f"Count: {count}")

# 5. Nested Loops - Loop inside a loop

print("\nNested Loop - Printing a grid:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # Move to next line after inner loop

# 6. Else Clause with Loops - Executes when loop is not terminated by 'break'

print("\nFor loop with else clause:")
for i in range(3):
    print(f"Loop iteration {i}")
else:
    print("This else is executed because the loop wasn't broken.")

# 7. Iterating Over a Dictionary

person = {"name": "Alice", "age": 25, "city": "Wonderland"}
print("\nFor loop - Iterating through a dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")
