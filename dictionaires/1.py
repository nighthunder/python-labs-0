# Dictionary with duplicate keys
duplicated_keys = {"key1": "value1", "key1": "value2", "key1": "value3"}

# Access key1
print(duplicated_keys["key1"])

# Create a Harry Potter dictionary
harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor"
}

# Display the dictionary
print(harry_potter_dict)

# Characters to add to the Harry Potter dictionary
add_characters_1 = {
    "Albus Dumbledore": "Gryffindor",
    "Luna Lovegood": "Ravenclaw"
}

# Merge dictionaries
harry_potter_dict.update(add_characters_1)

# Display the dictionary
print(harry_potter_dict)

# Use iterables to update a dictionary
add_characters_2 = [
    ["Draco Malfoy", "Slytherin"],
    ["Cedric Diggory", "Hufflepuff"]
]
harry_potter_dict.update(add_characters_2)

print(harry_potter_dict)

# Use iterables to update a dictionary
add_characters_3 = [
    ("Rubeus Hagrid", "Gryffindor"),
    ("Minerva McGonagall", "Gryffindor")
]
harry_potter_dict.update(add_characters_3)

print(harry_potter_dict)

# Delete a key:value pair
del harry_potter_dict["Minerva McGonagall"]

print(harry_potter_dict)

# Delete a key:value pair that doesn't exist in the dictionary
del harry_potter_dict["Voldemort"
