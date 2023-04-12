# Creating a tuple
fruits = ('apple', 'banana', 'orange')

# Accessing tuple elements
print(fruits[0])  # Output: 'apple'
print(fruits[1])  # Output: 'banana'
print(fruits[2])  # Output: 'orange'

# Looping through a tuple
for fruit in fruits:
    print(fruit)

# Attempting to modify a tuple (which will cause an error)
# fruits[0] = 'pear'  # Output: TypeError: 'tuple' object does not support item assignment
