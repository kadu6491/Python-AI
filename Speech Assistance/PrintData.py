from datetime import *
import datetime
import time
import requests
import webbrowser

from audio import *

# print_time = time.strftime('%H:%M')
# print_date = date.today()
# print(print_time)
# print(print_date)
# print(time.tzname)

a = AudioSetUp()
s = Speaker()


class FindData:
    @staticmethod
    def look_up_date():
        today = date.today()
        print(today)
        a.audio_date(today)

    @staticmethod
    def look_up_time():
        currentTime = datetime.datetime.now()
        zone = time.tzname

        x = str(currentTime.hour)
        y = str(currentTime.minute)
        print(x + ":" + y)
        a.audio_time(currentTime.hour, currentTime.minute, zone)

    def look_up_weather(self, city):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid="API ID HERE"&units=metric'.format(
            city)

        res = requests.get(url).json()

        # s.speech()

        temp = res['main']['temp']
        low_temp = res['main']['temp_min']
        high_temp = res['main']['temp_max']

        f = (temp * (9/5)) + 32
        l_f = (low_temp * (9/5)) + 32
        h_f = (high_temp * (9/5)) + 32

        hum = res['main']['humidity']
        des = res['weather'][0]['description']
        wind_speed = res['wind']['speed']

        print("Temperature: {} fahrenheit".format(int(f)))
        print("Humidity: {}%".format(hum))
        print("Weather: {}".format(des))
        print('Wind Speed : {} m/s'.format(wind_speed))
        a.audio_weather(des, int(f), int(l_f), int(h_f))

    def search(self, look):
        url = 'https://google.com/search?q=' + look
        webbrowser.get().open(url)
        a.audio_search(look)


# f = FindData()
# f.look_up_date()
# f.look_up_time()
# f.look_up_weather("Virginia Beach")
