# Define a function to check if a word has more than 5 characters
def has_more_than_5_chars(word):
    return len(word) > 5

# Create a list of words
words = ["apple", "banana", "cherry", "date", "fig", "grapefruit", "kiwi"]

# Use filter() to filter out words with more than 5 characters from the list
filtered_words = filter(has_more_than_5_chars, words)

# Convert the filter object to a list and print the result
print(list(filtered_words))  # Output: ['banana', 'cherry', 'grapefruit']
