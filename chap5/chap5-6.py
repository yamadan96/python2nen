import requests
import json

# 現在の天気を取得する：神戸
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe,JP", key="取得したAPIキー")

jsondata = requests.get(url).json()
print("都市名   = ", jsondata["name"])
print("気温　　 = ", jsondata["main"]["temp"])
print("天気　　 = ", jsondata["weather"][0]["main"])
print("天気詳細 = ", jsondata["weather"][0]["description"])
