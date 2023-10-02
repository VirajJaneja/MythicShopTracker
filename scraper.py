import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-16-notes/#patch-upcoming-skins-and-chromas'
url2 = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-18-notes/'

response = requests.get(url2)
soup = BeautifulSoup(response.content, "html.parser")
data = soup.find_all(string="Now Available")


target_text = "Prestige Star Guardian Ekko"

patch = 13.24

ul_elements = soup.find_all("ul")

mythicList = ul_elements[len(ul_elements)-3]
mythicList = mythicList.contents

try:
    with open('skins.json', 'r') as json_file:
        jsonData = json.load(json_file)
except FileNotFoundError:
    jsonData = {}

for skin in mythicList:
    title = skin.text
    print(title)
    if title not in jsonData:
        jsonData[title] = {
            "Price": 100,
            "Last Patch Appearance": patch,
            "Release Patch": patch
        }
    else:
        if(jsonData[title]["Last Patch Appearance"] != patch):
            jsonData[title]["Price"] = jsonData[title]["Price"] + 25
        if(jsonData[title]["Release Patch"] > patch):
            jsonData[title]["Release Patch"] = patch
        jsonData[title]["Last Patch Appearance"] = patch 

with open('skins.json', 'w') as json_file:
    json.dump(jsonData, json_file, indent=4)
# print(mythicList.contents[1].text)