#Ask the user what acronym they want to add
#Ask for definition
#Open the file
#Write

def add_acronym():
    acronym = input("What acronym do you want to add?\n")
    definition = input("What is the definition?\n")

    #with open("acronyms.txt", "w") as file:
    with open("acronyms.txt", "a") as file:
        file.write(acronym + " - " + definition + "\n")
    
def find_acronym():
    look_up = input("What software acronum would you like to look up?\n")

    found = False
    try:
        with open("acronyms.txt") as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError:
        print("File not found!")
        return
         
    if not found:
        print("The acronym does not exist")
                

# Main
def main():
    choice = input("Do you want to find(F) or add(A) an acronym?")
    if choice == "F":
        find_acronym()
    elif choice == "A":
        add_acronym()

main()
