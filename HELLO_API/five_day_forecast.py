import os
import requests
from datetime import date, datetime
from pprint import pprint

# set url, weather key, and query dictionary
url = 'https://api.openweathermap.org/data/2.5/forecast'
key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

if key is None:
    print('Unable to find WEATHER_KEY')

# make api request using url and query params
try:
    data = requests.get(url, params=query).json()

    # do stuff
    # make list of data
    list_of_forecasts = data['list']
    # loop through each item
    # and get the temperature and datetime
    for forecast in list_of_forecasts:
        temp = forecast['main']['temp']
        timestamp = forecast['dt']
        weather_description = forecast['weather'][0]['description']
        wind_speed = forecast['wind']['speed']
        # convert timestamp to a readable format (datetime)
        forecast_date = datetime.fromtimestamp(timestamp)
        # display
        print(f'At {forecast_date}, The weather will be {weather_description}, the temperature will be {temp} Fahrenheit,'
                f' wind speed projected to be {wind_speed} MPH')

except:
    print('Error: Unable to get data.')