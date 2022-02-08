import telebot;
from telebot import types
import json

bot = telebot.TeleBot('5068289217:AAGeuJKqN2bYezjE1bUx4i0nuz78dbvE_iQ1');

categories=['Одежда','Обувь','Аксессуары']
clothes=['Верхняя одежда','Худи и свитшоты','Футболки и майки','Штаны',"Шорты","Костюмы","Спортивные костюмы","Нижнее белье"]
pants=['Брюки',"Чиносы","Джинсы","Джоггеры","Спортивные штаны"]
setGetSizeFunction=['Ввести размер самостоятельно','Определить размер']
daNet=['Да','Нет']
typeOfSizes = ['Европейский', 'Русский', 'Американский']
genders = ['Мужчина', 'Женщина']
gender = ''
typeOfSize = ''


dial1 = 'Выбери одну из представленных категорий:\n\n(Для выбора категории введите номер рядом с категорией)'
dial2 = 'Я тебя не понимаю. Введи число.'
dial3 = 'Выберите тип размера'
dial4 = 'Выберите пол'
dial5 = 'Выберите размер'
sorry = 'Данная функция находится на этапе разработки. В скором времени она будет доступна.'


def getCat(categories,message,dial='Выберите один из вариантов'):
    keyboard = types.InlineKeyboardMarkup()
    for i in range(len(categories)):
        key_cat = types.InlineKeyboardButton(text=categories[i], callback_data=categories[i])
        keyboard.add(key_cat)
    bot.send_message(message.from_user.id, dial, reply_markup=keyboard )


def getSize(gender,typeOfSize):
    evroSize = []
    with open('dataSize.json', 'r') as j:
        sizes = json.load(j)
    for i in range(len(sizes)):
        size=sizes[i][gender][typeOfSize]
        if (not size in evroSize) and size != '':
            evroSize.append(size)
    return(evroSize)

@bot.message_handler(content_types=['text',])
def get_text_messages(message):
    if str(message.text).lower() == "/start":
        bot.send_message(message.from_user.id, "Привет, я ClothesBot. Я могу узнать твой размер и подобрать тебе вещи из различных интернет магзаинов, учитывая твои предпочтения.")
        bot.send_message(message.from_user.id, "Принцип моей работы прост-я отправляю тебе список категорий товаров, а ты выбираешь нужную из них.\n \nЧтобы выбрать категорию просто нажми на кнопку с нужной категорией.")
        getCat(categories,message,dial1)
    elif (message.text).isdigit():
        bot.send_message(message.from_user.id, 'вы ввели число')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == categories[0]: 
        getCat(clothes,call,dial1)
#
#категории
#
    elif call.data == categories[1]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == categories[2]:
        bot.send_message(call.from_user.id, sorry)
#
#одежда        
#
    elif call.data == clothes[0]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == clothes[1]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == clothes[2]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == clothes[3]:
        getCat(pants,call,dial1)
    elif call.data == clothes[4]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == clothes[5]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == clothes[6]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == clothes[7]:
        bot.send_message(call.from_user.id, sorry)
#
#штаны
#
    elif call.data == pants[0]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == pants[1]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == pants[2]:
        getCat(setGetSizeFunction,call)
    elif call.data == pants[3]:
        bot.send_message(call.from_user.id, sorry)
    elif call.data == pants[4]:
        bot.send_message(call.from_user.id, sorry)
#
#функция setGetSize
#
    elif call.data == setGetSizeFunction[0]:
        getCat(genders,call,dial4)
    elif call.data == setGetSizeFunction[1]:
        bot.send_message(call.from_user.id, sorry)
#
#выбор пола
#
    elif call.data in genders:
        global gender
        if call.data == 'Мужчина':
            gender='male'
        else:
            gender='female'
        getCat(typeOfSizes,call,dial3)
#
#выбор размера
#
    elif call.data in typeOfSizes:
        if call.data == 'Европейский':
            typeOfSize = 'evro'
        elif call.data == 'Русский':
            typeOfSize = 'rus'
        else:
            typeOfSize = 'USA'
        getCat(getSize(gender,typeOfSize),call,dial5)
        
    elif call.data in typeOfSizes:
        pass 
    else:
        bot.send_message(call.from_user.id, dial2)


bot.polling(none_stop=True, interval=0) 


# # Обработчик нажатий на кнопки
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     # Если нажали на одну из 12 кнопок — выводим гороскоп
#     if call.data == "zodiac": 
#         # Формируем гороскоп
#         msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
#         # Отправляем текст в Телеграм
#         bot.send_message(call.message.chat.id, msg)
# # Запускаем постоянный опрос бота в Телеграме
# bot.polling(none_stop=True, interval=0)



