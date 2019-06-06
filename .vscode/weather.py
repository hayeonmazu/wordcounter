import json
import requests

r=requests.get("https://api2.sktelecom.com/weather/summary?version=2&lat=%2037.47626486935654&lon=126.98136872618234&appkey=69aa6bbb-896a-4845-9469-15a732e16750")

data=json.loads(r.text)
weather=data["weather"]["summary"]
cTime=weather[0]["timeRelease"]
cSky=weather[0]["yesterday"]["sky"]["name"]

cWeather="오늘은"+cTime+ "\n 하늘은"+cSky
print(cWeather)