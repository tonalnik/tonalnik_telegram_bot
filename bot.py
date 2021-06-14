from romb import *
import telebot
import pyowm
import time
import json

with open('./telegram_token.json', encoding = 'UTF-8') as file:
    telegram_token = json.load(file)

owm = pyowm.OWM('37656453f70fc458f65d30166b29610d')
bot = telebot.TeleBot(telegram_token['id'])
mgr = owm.weather_manager()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Ну начнём, если хочешь узнать список комманди пиши "/help"')

@bot.message_handler(content_types=['text'])
def send_text(message):
    f = open('fails_log.txt', 'a')

    f_name = message.from_user.first_name
    l_name = message.from_user.last_name
    if str(l_name) == "None":
        l_name = ''

    text = message.text
    text = text.lower()
    
    if text == 'привет':
        bot.send_message(message.chat.id, 'Ку')
    elif text == 'пока':
        bot.send_message(message.chat.id, 'Бб')
    elif text == 'извинись':
        bot.send_message(message.chat.id, 'Сам извинись')
    elif text == 'пошли меня нахуй':
        answer = 'Пошёл нахуй, ' + str(f_name) + ' ' + str(l_name)
        bot.send_message(message.chat.id, answer)
    elif text == 'погода':
        bot.send_message(message.chat.id, 'В каком городе?')
        #Пошаговый обработчик
        bot.register_next_step_handler(message, weather)

    elif text == 'гуль' or text == 'deadinside' or text == '1000-7' or text == 'ghoul' or text == 'дединсайд' or text == 'zxc' or text == 'zxcursed':
        bot.send_message(message.chat.id, "???")
        time.sleep(1)
        bot.send_photo(message.chat.id, 'https://sun9-14.userapi.com/impg/lziS0NmpK9fsXAmxMdWcO-8Ck2JeVpWZGKxKfg/zbx9cSJsRhU.jpg?size=480x320&quality=96&sign=569385192284a463a657308d66e8a5a1&type=album');
        time.sleep(2)
        k = 0
        for i in range(1000, 0, -7):
            if i > 40:
                if k != 0 and k % 3 == 0:
                    k += 1
                    continue
                k += 1
            bot.send_message(message.chat.id, i)
        answer =  'fuck fuck фак? 1000-7 ? что ахахах что ыт сказал ? 993 хавфвхавахыфывах xDxd wtF ) ghoul ghoul m0d aktivейтеdx d[d[d[­[фыуа хвхваыххав ых fuckckck kzxxdd вас никто не слы? что ? хваыхфывахыва XD)DD) fuck fuck fcuk s;s;s;s;s;s;s; pf44f4f4f 3p33p3p shi1ttt dldldldldldl sslslsl wanna d1e? doldldld die die1 die? dopdodododpdp fudk ghoul ghoul/ / / /sghhkhhkhklhk ,. . .. . . . .3p3p3pp3p3 sssssssss я... гуль XD)D)D)D fuck fcu k lobby lobyy king 6k main 4250 smurf fuck fuck fuck ты хочешь сыграть лобак? ты же и mинуты не простоишь ? cht о ахавыхфх wTF fuc kfcu klds;.s;s;; you wanna ? play? l00000000BY? ? ? ? ?? ? ? . . . 19000 - 7-777 7-07 -7-7 -7- 70 1 0 9 9 9 393 933? ?339 3 93 93 3 тату на лбу dead ins1de damn bro wtf sosklslslslsks kfuic fuck sorrry sorry sorry ,. ,. ,. . sorry . .. ,,34, shititititti tiktigikgik kfuckfucfkcukfufs 100-70 -7 070 7-1 1010 101 -7- 70 ssiiei syкa маtемати4kf pft,fkf ghjcnj cerf pft,fkf Z [JXE EVTHTNM GJVJUBNT GJVJUBNT FGPSFAP[D[ASDF[ASDF[ADF 4kdkddkdk djdkfkfid wannf die lddl wanna die wannadied kdkadjkdkae 3annwadie wanna aDE1'
        bot.send_message(message.chat.id, answer)
    elif text == 'ромб' or text == 'romb':
        bot.send_message(message.chat.id, 'Введите сторону ромба: ')
        bot.register_next_step_handler(message, teleromb)

    elif text == '/help' or text == "help" or text == "помощь":
        bot.send_message(message.chat.id, 
        'Список доступных комманд (регистр не имеет значение):\n'
        'Привет\n'
        'Пока\n'
        'Извинись\n'
        'Пошли меня нахуй\n'
        'Погода\n'
        #'Ромб (romb)\n'
        'zxc (1000-7)\n'
        )

    else:
        answer = 'Я тебя не понял!'
        bot.send_message(message.chat.id, answer)
        if len(text) < 100:
            f.write(str(f_name) + " " + str(l_name) + " | " + text + "\n")
        f.close()

def weather(message):
    try:
        text = message.text
        text = text.title()

        observation = mgr.weather_at_place(message.text)
        w = observation.weather

        #температура
        t = w.temperature("celsius")
        t_middle = t['temp']
        t_feels = t['feels_like']
        #скорость ветра
        wind = w.wind()['speed']
        #влажность
        h = w.humidity
        #время
        weather_time = w.reference_time('iso')
        time = weather_time.split()
        time_hours = time[1].split(':')
        time_hours[0] = str((int(time_hours[0]) + 3) % 24)

        answer = ('На момент ' + time[0] + ' ' + time_hours[0] + ':' + time_hours[1] + 
            '\nВ городе ' + text + ' сейчас ' + str(abs(int(t_middle))) + '°C, ощущается как ' + 
            str(abs(int(t_feels))) + '°C\nСкорость ветра ' + str(wind) + 
            'м/c, относительная влажность ' + str(h) + '%')

        bot.send_message(message.chat.id, answer)
        
    except pyowm.commons.exceptions.NotFoundError:
        bot.send_message(message.chat.id, 'Ошибка, город не найден')


def teleromb(message):
    v = int(message.text)
    a = [1, 2, 3, 4, 5]
    if (v > 0):
        s = romb(v)
        for i in range(v*2-1):
            bot.send_message(message.chat.id, str(a))
    else:
        bot.send_message(message.chat.id, 'Введите число больше нуля!')

bot.polling(none_stop=True)
