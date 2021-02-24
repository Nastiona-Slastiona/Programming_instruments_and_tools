from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('b995cefbcf08a1a6c8426b835ffc5a1c',config_dict)
mgr = owm.weather_manager()

place = input("Введите город\страну:  ")

observation = mgr.weather_at_place(place)
weather = observation.weather

print(" Температура сейчас: "+ str(weather.temperature('celsius')['temp'])+" С° \n")

if weather.temperature('celsius')['temp'] <= 0:
    print("\t На улице довольно таки холодно, не забудь шапку!\n")
elif weather.temperature('celsius')['temp'] < 10:
    print("\t Прохладно, но можно без шапки. \n")
elif weather.temperature('celsius')['temp'] < 20:
    print("\t Тепло, но лучше что-нибудь накинуть на плечи.\n")
elif weather.temperature('celsius')['temp'] < 30:
    print("\t Жарковато, прихвати с собой воды.\n")
else:
    print("Очень жарко, не забудь намазать кожу защитным кремом иначе сгоришь...")
