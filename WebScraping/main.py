import pandas as pd
import requests
from bs4 import BeautifulSoup

# We need to install Beautifulsoap4, requests and panda through pip, then only we can implement these lines of code!


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.9198&lon=-86.2818#.X0TsF8hKjDc')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

#print(week)

items = week.find_all(class_='tombstone-container')

#print(items[0])

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]

short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
print(period_names)
print(short_descriptions)
print(temperatures)

# some cool stuff with pandas--

weather_stuff = pd.DataFrame({
        'periods': period_names,
        'short_descriptions': short_descriptions,
        'temperatures': temperatures,
    })

print(weather_stuff)

# creating csv file--

# thats how we can create csv file using panda... but now i hv taken this line into comment...
# thts a very powerful stuff...
#weather_stuff.to_csv('weather.csv')

# thats how we can create csv file using panda... but now i hv taken this line into comment...



