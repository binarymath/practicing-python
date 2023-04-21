from functools import reduce

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce() to find the product of the numbers in the list
product = reduce(multiply, numbers)

print(product)  # Output: 120
