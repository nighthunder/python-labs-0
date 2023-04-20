# Ask the user for a list of three friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to the nearby_friends.txt file

for x in range(3):
    user_input = input('Say a friend\'s name')
    people_file = open('people.txt', 'r')
    nearby_file = open('nearby_friends.txt', 'w')
    content = people_file.readlines()
    people_file.close()
    for name in content:
        if user_input == name:
            nearby_file.write(name)
            nearby_file.write('\n')
    nearby_file.close()
    
