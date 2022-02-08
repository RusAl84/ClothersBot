import json

fileObject = open("data.json", "r", encoding="UTF-8")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)

