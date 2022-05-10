# Introduction to Class
#   - Introduction to Object-Oriented Programming (OOP)

class Animal:
    # Constructor
    #   - Creates a new Animal object
    def __init__(self, name: str):
        self.name = name
        self.colour = ""
        self.age = 0                # in years
        self.weight = 0             # in kgs

        print("Created a new Animal")

    def breathe(self):
        print(f"{self.name} breathes in and out")

class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

        self.sassy = True

    def meow(self):
        print("Meow")
        print(f"Hi my name is {self.name}")

    def breathe(self):
        print(f"{self.name} purrs as it breathes")

class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

        self.loyal_friend = True

    def bark(self):
        print(f"{self.name} lets out a bark!")

    def breathe(self):
        print(f"{self.name} pants")


# Create a new Animal

fred = Animal("Fred") # this is a call to __init__()

print(type(fred))

# Change fred's properties
fred.colour = "Blue"
fred.age = 13
fred.weight = 5
fred.breathe()

fran = Animal("Fran")
fran.breathe()

# Create a new Cat object

chester = Cat("Chester")
chester.breathe()
chester.meow()

# Create a new Dog object
Ruffles = Dog("Ruffles")
Ruffles.breathe()
Ruffles.bark()

class Mr_Anderson:
    def __init__(self):
        self.name = "Mr. Anderson"
        self.personality = ""

    def bassDrum(self):
        while True:
            print("BOOM")


teacher = Mr_Anderson()

teacher.bassDrum()