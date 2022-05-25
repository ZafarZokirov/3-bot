import requests
from Cfg import open_weather
import requests
from pprint import pprint


def get_weather(city, token):
    try:
        result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}")
        data = result.json()
        pprint(data)
        shahar = data["name"]
        temp = data["main"]["temp"]
        namlik= data["main"]["humidity"]
        tezlik=data["wind"]["speed"]
        print(f"shahar {shahar}\n"
              f"temp {temp}\n"
              f"namlik {namlik}\n"
              f"tezlik {tezlik}\n")
    except Exception as ex:
        pass
def main():
    city = input("Shahar nomi kirit:")
    get_weather(city, open_weather)
main()

































