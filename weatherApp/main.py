import requests
import json

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=d510ef7eff7f4350b0a111127260602&q={city}"

r = requests.get(url)
# print(r.text)
if r.status_code == 200:
    wdic = json.loads(r.text)
    print(f"Weather in {city} in degree celcius is: ", wdic["current"]["temp_c"])
else:
    print(r.text)
