# ----------------------------------------------------------
# https://github.com/natnew/Python-Projects-Get-Weather-Data

import requests
from pprint import pprint

API_Key = " " # Put your Key Here

Ciudad = input("Enter City: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + Ciudad

weather_data = requests.get(base_url).json()

pprint(weather_data)