#Example URL
# https://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&appid=5f08e7540ce485cae94772b789bb7365
import os 
import requests
from pprint import pprint
from datetime import datetime

key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us','units': 'imperial','appid': key }
url = ' https://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()
pprint(data)

list_of_forecasts = data['list']

for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    timestamp = forecast ['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f'At {forecast_date} the temparature will be {temp}F')