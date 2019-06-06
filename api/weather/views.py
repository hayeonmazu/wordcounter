from django.shortcuts import render
import json
import requests

def home(request):
    r = requests.get("https://api2.sktelecom.com/weather/summary?version=2&lat= 37.47626486935654&lon=126.98136872618234&appkey=69aa6bbb-896a-4845-9469-15a732e16750")
    data=json.loads(r.text)
    weather1= data["weather"]["summary"]
    cTime= weather1[0]["timeRelease"]
    cPlace=weather1[0]['gird']['city']+''+weather1[0]['gird']['country']+''+weather1[0]['gird']['village']
    cSky=weather1[0]['today']['sky']['name']

    return render(request, 'home.html', {'cSky':cSky, 'cPlace':cPlace,'cTime':cTime})