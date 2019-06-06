import requests
from bs4 import BeautifulSoup

Tag = '#content > form > div > table > tbody > tr > td.tl > a'
URL ='http://gachon.ac.kr/community/opencampus/03.jsp?boardType_seq=358'

req = requests.get(URL)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

all_a= soup.select(Tag)
for title in all_a:
    print(title.text)