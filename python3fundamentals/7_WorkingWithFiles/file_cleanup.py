import os

folder = "C:/"

entries = os.scandir(folder)

for entry in entries:
    if os.path.isfile(entry):
        print("File:", entry.name)
    elif os.path.isdir(entry):
        print("Directroy:", entry.name)
