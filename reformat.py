import json

baseJson = 'SEASON12.json'

try:
    with open(baseJson, 'r') as json_file:
        jsonData = json.load(json_file)
except FileNotFoundError:
    jsonData = {}

targetJson = 'SEASON13.json'

try:
    with open(targetJson, 'r') as json_file:
        targetData = json.load(json_file)
except FileNotFoundError:
    targetData = {}




for skin, skin_data in jsonData.items():
    entry = skin_data["Release Patch"]
    appearances = skin_data["Appearances"]

    targetData[skin] = {
        "First Mythic Shop Appearance": entry,
        "2nd Appearance": "0.0",
        "3rd Appearance": "0.0",
        "4th Appearance": "0.0",
        "5th Appearanace": "0.0",
        "Total Appearances": appearances
    }




with open(targetJson, 'w') as json_file:
    json.dump(targetData, json_file, indent=4)