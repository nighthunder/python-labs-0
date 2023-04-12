# Define a lambda function to square a number
square = lambda x: x**2

# Call the lambda function to square a number
result = square(5)
print(result)   # Output: 25

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use a lambda function with the 'map' function to square each number in the list
squares = list(map(lambda x: x**2, numbers))

# Print the resulting list of squared numbers
print(squares)  # Output: [1, 4, 9, 16, 25]
