class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("The {} says hello!".format(self.species))

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "cat")
        self.breed = breed

    def speak(self):
        print("{} the {} says meow!".format(self.name, self.breed))

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "dog")
        self.breed = breed

    def speak(self):
        print("{} the {} says woof!".format(self.name, self.breed))

# Create some animals
my_cat = Cat("Whiskers", "Siamese")
my_dog = Dog("Fido", "Labrador")

# Make them speak
my_cat.speak()
my_dog.speak()
