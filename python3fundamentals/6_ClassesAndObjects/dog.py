class Robot_Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("Woof woof!")
        
# Main program
my_dog = Robot_Dog("Spot", "Samojed")
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()