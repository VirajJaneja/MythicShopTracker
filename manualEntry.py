import json

baseJSON = 'SEASON13.json'

try:
    with open(baseJSON, 'r') as json_file:
        jsonData = json.load(json_file)
except FileNotFoundError:
    jsonData = {}


def doJsonProcess(patch, title):
    if title not in jsonData:
        jsonData[title] = {
        "First Mythic Shop Appearance": patch,
        "2nd Appearance": "0.0",
        "3rd Appearance": "0.0",
        "4th Appearance": "0.0",
        "5th Appearanace": "0.0",
        "Total Appearances": 1
        }
    else:
        if(jsonData[title]["2nd Appearance"] == "0.0"):
            jsonData[title]["2nd Appearance"] = patch
        elif(jsonData[title]["3rd Appearance"] == "0.0"):
            jsonData[title]["3rd Appearance"] = patch
        elif(jsonData[title]["4th Appearance"] == "0.0"):
            jsonData[title]["4th Appearance"] = patch
        elif(jsonData[title]["5th Appearanace"] == "0.0"):
            jsonData[title]["5th Appearanace"] = patch
        jsonData[title]["Total Appearances"] += 1

    with open(baseJSON, 'w') as json_file:
        json.dump(jsonData, json_file, indent=4)

while(True):
    skin = input("Enter: ")

    if skin.lower() == 'exit':
        break

    patch, skin = map(str.strip, skin.split('-', 1))
    doJsonProcess(patch, skin)

