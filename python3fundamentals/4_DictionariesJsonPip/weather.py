import requests

city = "Sombor"
url = "http://api.weatherapi.com/v1/current.json?key=2dfef7e19ab2450eafa103650240711&q="+city+"&aqi=no"
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get("current").get("temp_c")
description = weather_json.get("current").get("condition").get("text")

print("Today's weather in", city, "is", description, "and", temp, "degrees")
