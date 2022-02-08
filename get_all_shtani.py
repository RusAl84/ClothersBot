import json

def pjson(item):
    str1="Производитель: "+ item['brand'] + " Цвет: " + item['color'] + ""\
        " Стоимость: " + str(item['cost']['dollar']) +"$ " + str(item['cost']['rub'])  + " р."\
        "\n Ссылка: " + item['link'] + "\n"
    for item1 in item['items']:
        str1+=f"Пол: {item1['gender']}clc Размеры: USA:{item1['USA']} EVRO:{item1['evro']} RUS:{item1['rus']} \n"
    return str1

def get_all_shtani():
    fileObject = open("data2.json", "r", encoding = "UTF-8")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    str1 = ""
    for item in ListOfItem:
        str1 += pjson(item) + "\n"
    return str1

if __name__ == '__main__':
    l = get_all_shtani()
    print(l)