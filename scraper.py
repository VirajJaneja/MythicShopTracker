import requests
from bs4 import BeautifulSoup

url = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-16-notes/#patch-upcoming-skins-and-chromas'
url2 = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-1-notes/'

response = requests.get(url2)
soup = BeautifulSoup(response.content, "html.parser")
data = soup.find_all(string="Now Available")


target_text = "Prestige Star Guardian Ekko"

ul_elements = soup.find_all("ul")

desired_ul_element = ul_elements[len(ul_elements)-3]

print(desired_ul_element)