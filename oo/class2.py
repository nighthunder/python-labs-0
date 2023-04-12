class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print("The car is now going {} mph".format(self.speed))

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
            print("The car is now going {} mph".format(self.speed))
        else:
            self.speed = 0
            print("The car is now stopped")

    def get_info(self):
        return "{} {} ({})".format(self.make, self.model, self.year)

my_car = Car("Honda", "Civic", 2020)
print(my_car.get_info())

my_car.accelerate()
my_car.accelerate()
my_car.brake()
my_car.brake()
my_car.brake()
