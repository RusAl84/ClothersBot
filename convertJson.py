import json

fileObject = open("data.json", "r", encoding="UTF-8")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)

jsonString = json.dumps(aList, ensure_ascii=False, indent=4, sort_keys=True)
jsonFile = open("data2.json", "w", encoding="UTF-8")
jsonFile.write(jsonString)
jsonFile.close()
