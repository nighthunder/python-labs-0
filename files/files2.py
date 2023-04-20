# Ask the user for a list of three friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to the nearby_friends.txt file

friends = input('Enter three friends names, separated by commas (no space, please):').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()] # remove \n
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

""" print(f'FRIENDS {friends_nearby_set}')
print(f'NEARBY {friends_nearby_set}') """

friends_nearby_set = friends_set.intersection(people_nearby_set)

friends_nearby_file = open('nearby_friends.txt', 'w')

print(friends_set)
print(people_nearby)
print(friends_nearby_set)

for friend in friends_nearby_set:
    print(f'{friend} is nearby!  Meet up with them')
    friends_nearby_file.write(f'{friend}\n')

friends_nearby_file.close()