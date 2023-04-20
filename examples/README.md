# Main differences between filter and map #

filter() and map() are both built-in functions in Python that are used for transforming or processing data in collections like lists, but they serve different purposes and have some key differences.

## Functionality: ##
 filter() is used to filter elements from a collection based on a given condition, whereas map() is used to apply a function to each element in a collection and create a new collection of the results.

## Output: ##
 filter() returns a filter object, which is an iterator that produces the filtered elements one at a time when iterated upon, or it can be converted to a list using list() function. On the other hand, map() returns a map object, which is also an iterator that produces the mapped elements one at a time when iterated upon, or it can be converted to a list using list() function.

## Input Function: ##
 The function used in filter() should return a boolean value (True or False) to determine whether an element should be included in the filtered output. The function used in map(), on the other hand, can return any value and is applied to each element in the input collection.

Input Collection: Both filter() and map() take a collection (e.g., list, tuple) as input, but the collection can be of any type and size for both functions.

## Usage: ##
 filter() is commonly used when you want to filter out elements from a collection based on a condition, such as filtering out even numbers, odd numbers, or elements that satisfy a certain criteria. map(), on the other hand, is commonly used when you want to apply a function to each element in a collection and create a new collection of the results, such as applying a mathematical operation to a list of numbers or converting a list of strings to uppercase.

In summary, filter() is used to filter elements from a collection based on a condition, while map() is used to apply a function to each element in a collection and create a new collection of the results.