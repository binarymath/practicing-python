# Define a function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to filter out even numbers from the list
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list and print the result
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]
