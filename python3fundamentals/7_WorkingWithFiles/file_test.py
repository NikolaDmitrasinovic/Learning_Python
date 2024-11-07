with open("acronyms.txt") as file:
    #result = file.readlines()
    #for line in result:
    for line in file:
        print(line)

look_up = input("What software acronum would you like to look up?\n")

found = False
with open("acronyms.txt") as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break
        
if not found:
    print("The acronym does not exist")
