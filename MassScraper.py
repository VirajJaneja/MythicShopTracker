import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-16-notes/#patch-upcoming-skins-and-chromas'
url2 = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-8-notes/'
url2 = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-12-6-notes/'
url2 = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-12-14-notes/'



#gets the 
response = requests.get(url2)
soup = BeautifulSoup(response.content, "html.parser")
data = soup.find_all(string="Now Available")


patch = 0.0

ul_elements = soup.find_all("ul")


keyword = "prestige"
prestige_indices = [index for index, element in enumerate(ul_elements) if keyword in element.text.lower()]

mythicExists = False

if(len(prestige_indices) != 0):
    mythicExists = True

    
# 'prestige_indices' now contains the indices of elements with the keyword "prestige" in their text


#collects and adds the names to json from list mythicList
def doJsonProcess(mythicListInput):
    try:
        with open('skins.json', 'r') as json_file:
            jsonData = json.load(json_file)
    except FileNotFoundError:
        jsonData = {}

    for skin in mythicListInput:
        title = skin.text.split('++++')[0].strip()
        title = title.split('(125')[0].strip()
        title = title.split('(150')[0].strip()
        title = title.split('(100')[0].strip()
        title = title.split('(175')[0].strip()
        title = title.split('(200')[0].strip()
        title = title.split(':')[0].strip()




        print(title)
        if title not in jsonData:
            jsonData[title] = {
                "Price": 100,
                "Last Patch Appearance": patch,
                "Release Patch": patch,
                "Appearances": 1
            }
        else:
            if(jsonData[title]["Last Patch Appearance"] != patch):
                jsonData[title]["Price"] = jsonData[title]["Price"] + 25
            if(jsonData[title]["Release Patch"] > patch):
                jsonData[title]["Release Patch"] = patch
            jsonData[title]["Last Patch Appearance"] = patch 
            jsonData[title]["Appearances"] =  jsonData[title]["Appearances"] + 1

    with open('skins.json', 'w') as json_file:
        json.dump(jsonData, json_file, indent=4)


# #season 12 scraper process
for i in range(11):
    url = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-12-'+(str)(13+i)+'-notes/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all(string="Now Available")


    patch = 12 + (8+i)*.1
    if((8+i)*.01>12.01):
        patch = 1+((8+i)*.01)
    

    patch = "12."+ (str)(13+i)
    print(patch)
    print(url)

    ul_elements = soup.find_all("ul")


    keyword = "prestige"
    prestige_indices = [index for index, element in enumerate(ul_elements) if keyword in element.text.lower()]

    mythicExists = False

    if(len(prestige_indices) != 0):
        mythicExists = True

    if(mythicExists):
        mythicList = ul_elements[prestige_indices[0]]
        mythicList = mythicList.contents
        print(patch)
        doJsonProcess(mythicList)



#season 13 scraper process
# for i in range(17):
#     url = 'https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-'+(str)(3+i)+'-notes/'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     data = soup.find_all(string="Now Available")


#     patch = "13."+ (str)(3+i)
#     print(patch)
#     print(url)

#     ul_elements = soup.find_all("ul")


#     keyword = "prestige"
#     prestige_indices = [index for index, element in enumerate(ul_elements) if keyword in element.text.lower()]

#     mythicExists = False

#     if(len(prestige_indices) != 0):
#         mythicExists = True

#     if(mythicExists):
#         mythicList = ul_elements[prestige_indices[0]]
#         mythicList = mythicList.contents
#         print(patch)
#         doJsonProcess(mythicList)

# # print(mythicList.contents[1].text)