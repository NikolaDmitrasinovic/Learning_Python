def greetings(name):
    print("Hello", name)

"""    
def greetings():
    print("Hello", name)
"""  

# Main program
name1 = input("Enter your name:\n")
greetings(name1)
name2 = input("Enter your name:\n")
greetings(name2)

"""
name = input("Enter your name:\n")
greetings()
"""

# addition
def addition(a, b):
    return a + b

def main():
    num1 = float(input("Enter a:\n"))
    num2 = float(input("Enter b:\n"))

    result = addition(num1, num2)
    print("result:", result)
    
main()
