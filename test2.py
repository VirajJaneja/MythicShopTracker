import json
import requests
from bs4 import BeautifulSoup

url2 = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-12-19-notes/'

url2 = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-12-14-notes/'
#12-23
url2 = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-24-notes/'

response = requests.get(url2)
soup = BeautifulSoup(response.content, "html.parser")
print(soup)

with open('soup_content3.txt', 'w', encoding='utf-8') as file:
    file.write(str(soup))
