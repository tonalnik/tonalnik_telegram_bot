from romb import *
import json
import os
heroku_token = os.environ.get('BOT_TOKEN')

v = int(input('Введите сторону ромба: '))
if (v > 0):
    s = romb(v)
    for i in range(v*2-1):
        print(*s[i], sep = '')
else:
    print ('Введите число больше нуля!')
