from romb import *
import json

with open('./telegram_token.json', encoding = 'UTF-8') as file:
    telegram_token = json.load(file)

v = int(input('Введите сторону ромба: '))
if (v > 0):
    s = romb(v)
    for i in range(v*2-1):
        print(*s[i], sep = '')
else:
    print ('Введите число больше нуля!')

print(telegram_token['id'])