contacts = {
    "number": 4,
    "students":
        [
            {"name":"Pera Kojot", "email":"kojot@dot.com"},
            {"name":"Tica Trkacica", "email":"trkacica@dot.com"},
            {"name":"Patak Daca", "email":"daca@dot.com"},
            {"name":"Dusko Dugousko", "email":"dugousko@dot.com"}
        ]
}
    
print("Students emails:")
for student in contacts["students"]:
    print(student["email"])
    