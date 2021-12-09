import telebot
from telebot import types
from openpyxl import load_workbook
import datetime
import locale

weeks = [
    'понедельник',
    'вторник',
    'среда',
    'четверг',
    'пятница',
    'суббота',
]

def current_date():
    locale.setlocale(locale.LC_ALL, "ru")
    day = datetime.datetime.today().strftime("%A")
    week = 15
    return day , week

def next_day():
    locale.setlocale(locale.LC_ALL, "ru")
    date = datetime.datetime.today()  
    date += datetime.timedelta(days=1)
    day = date.strftime("%A")
    week = 15
    return day , week

def get_schedule(day):
    wb = load_workbook('5\р2.xlsx')
    sheet = wb['Лист1']
    result = []
    if day == 'понедельник':
        s = 2
        result = []
        for n , i in enumerate(range(s , 21 , 2)):
            if n % 2 == 0:
                data = str(sheet['B{0}'.format(i)].value) + ' ' + str(sheet['D{0}'.format(i)].value)
                result.append(data)

    elif day == 'вторник':
        s = 22
        result = []
        for n , i in enumerate(range(s , 41 , 2)):
            if n % 2 == 0:
                data = str(sheet['B{0}'.format(i)].value) + ' ' + str(sheet['D{0}'.format(i)].value)
                result.append(data)

    elif day == 'среда':
        s = 42
        result = []
        for n , i in enumerate(range(s , 61 , 2)):
            if i == 52:
                print('yoy')
            if n % 2 == 0:
                data = str(sheet['B{0}'.format(i)].value) + ' ' + str(sheet['D{0}'.format(i)].value)
                result.append(data)
        print(result)
    elif day == 'четверг':
        s = 62
        result = []
        for n , i in enumerate(range(s , 81 , 2)):
            if n % 2 == 0:
                data = str(sheet['B{0}'.format(i)].value) + ' ' + str(sheet['D{0}'.format(i)].value)
                result.append(data)

    elif day == 'пятница':
        s = 82
        result = []
        for n , i in enumerate(range(s , 101 , 2)):
            if n % 2 == 0:
                data = str(sheet['B{0}'.format(i)].value) + ' ' + str(sheet['D{0}'.format(i)].value)
                result.append(data)

    elif day == 'суббота':
        s = 102
        result = []
        for n , i in enumerate(range(s , 121 , 2)):
            if n % 2 == 0:
                data = str(sheet['B{0}'.format(i)].value) + ' ' + str(sheet['D{0}'.format(i)].value)
                result.append(data)

    rresult = []
    for n , i in enumerate(result):
        if not 'None' in i:
            rresult.append(str(n+1) + ' ' + i)
    return rresult
    
def message_from_schedule(schedule):
    if len(schedule) == 0:
        return 'Нет занятий'
    return '\n'.join(schedule)

token = '5019029454:AAEW4j1cfYvU4uSgjoNLXm2IQALZ8cdPnNY'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button1 = types.KeyboardButton("Сегодня")
    button2 = types.KeyboardButton("Завтра")
    button3 = types.KeyboardButton("Выбрать день")
    keyboard.add(button1,button2 , button3)

    if message.text == 'Сегодня':
        bot.send_message(message.from_user.id, message_from_schedule(get_schedule(current_date()[0])) , reply_markup = keyboard)
    if message.text == 'Завтра':
        bot.send_message(message.from_user.id, message_from_schedule(get_schedule(next_day()[0])) , reply_markup = keyboard)
    if message.text == 'Выбрать день':
        bot.send_message(message.from_user.id, "Выберите день недели" , reply_markup = keyboard)

    if message.text.lower() in weeks:
        bot.send_message(message.from_user.id, message_from_schedule(get_schedule(message.text.lower())) , reply_markup = keyboard)



bot.polling(none_stop=True, interval=0)
