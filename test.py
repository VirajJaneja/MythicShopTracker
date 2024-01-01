import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-16-notes/#patch-upcoming-skins-and-chromas'
url2 = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-14-14-notes/'




#gets the 
response = requests.get(url2)


if "404" in response.content.decode("utf-8"):
    print("404 Error: Page not found.")
else:
    # Parse the content if the page was found
    soup = BeautifulSoup(response.content, "html.parser")
    print("working")