import requests
import json
import pyttsx3
engine = pyttsx3.init()

city=input("Enter the name of the city\n")
url=f"https://api.weatherapi.com/v1/current.json?key=dc383f74d6924079b9b121110242204&q={city}"
r=requests.get(url)
print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
engine.say(f'the current weather in {city } is {w} degrees')
engine.runAndWait()