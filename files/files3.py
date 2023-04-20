try:
    questions = open('nearby_friends.txt', 'r')
    content = questions.readlines()
    while True:
        for question in content:
            print(question + "\n")
            try:
                answer = int(input("Write down bellow the answer (only integers numbers)."))
            except ValueError:
                print("Only integers numbers are allowed.")
            except:
                print("An error has ocurred trying to get the input.")

except IOError:
    print("Could not read the file.")
except:
    print("An error has ocurred.")