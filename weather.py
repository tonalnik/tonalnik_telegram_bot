import pyowm

owm = pyowm.OWM('37656453f70fc458f65d30166b29610d')
mgr = owm.weather_manager()

place = input("В каком городе?: ")
observation = mgr.weather_at_place(place)
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
time_hours[0] = str((int(time_hours[0]) + 4) % 24)
print(time[0] + ' ' + time_hours[0] + ':' + time_hours[1])
print(time_hours)
print(weather_time)

print(abs(int(t_middle)), abs(int(t_feels)))