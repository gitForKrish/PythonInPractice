class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    
    def description(self):
        print(f"My Dog name is {self.name}. Dog's color is {self.color}. Dog's age is {self.age}")

    def sit(self):
        print(f"{self.name} is sitting now.")
    
    def shout(self):
        print("Bark barkkk...")

my_dog = Dog('Jack', 'White', '4')
my_dog.description()
my_dog.shout()
my_dog.sit()

your_dog = Dog('Kalu','Black','8')
my_dog.sit()
my_dog.shout()
my_dog.description()

