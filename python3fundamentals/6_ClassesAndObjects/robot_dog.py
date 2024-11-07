#dog
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print("My name is", self.name)
        
    def walk(self, x):
        self.position[0] = self.position[0] + x    
        print("New position:", self.position)
        
    def eat(self):
        print("I'm hungry!")

# robot dog
class Robot_Dog(Robot):
    def make_noise(self):
        print("Woof woof!")
        
    def eat(self):
        super().eat()
        print("I like bacon!")

# Main
my_robot_dog = Robot_Dog("Bud")
my_robot_dog.eat()
my_robot_dog.walk(10)
my_robot_dog.make_noise()
