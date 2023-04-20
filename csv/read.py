file = open('students.csv','r')
lines = file.readlines()
file.close

lines = [line.strip() for line in lines[1:]] # list slicing removing \n inside the strings and the header

for line in lines:
    person_data = line.split(',')
    name = person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree = person_data[3]

    print(f"{name.title()} is {age}, studying {degree.capitalize()} at {university.title()}")
