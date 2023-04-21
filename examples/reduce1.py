from functools import reduce

# Define a function to add two numbers
def add(x, y):
    return x + y

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce() to sum up the numbers in the list
sum = reduce(add, numbers)

print(sum)  # Output: 15
