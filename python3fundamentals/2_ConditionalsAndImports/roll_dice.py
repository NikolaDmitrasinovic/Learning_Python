import random

roll = random.randint(1,6)

# print("rolled a: " + str(roll))

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("Correct! The roll is: " + str(roll))
else:
    print("Wrong!")