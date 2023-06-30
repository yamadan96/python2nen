import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.yahoo.co.jp/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

topic = soup.find(class_="_2jjSS8r_I9Zd6O9NFJtDN-")
for element in topic.find_all("a"):
    print(element.text)


