import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

numberInSpace = json["number"]

print("There are", numberInSpace, "people in space right now and they are:")
for person in json["people"]:
    print(person["name"])
