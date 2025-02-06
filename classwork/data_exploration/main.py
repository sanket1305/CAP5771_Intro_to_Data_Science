import json
import urllib
import urllib.request

import io
import pandas as pd

# function to fetch data from any URL
def fetchdata(url, isjson=True):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://www.google.com/',
        'DNT': '1',  # Do Not Track request header
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        if isjson:
            return json.loads(data)
        else:
            return data

# send the request to URL to get latitude, longitude for our desired location
url = "https://nominatim.openstreetmap.org/search.php?q=Compton%2C+California&format=json"
json_data = fetchdata(url)

# store the result in a json file
print(json_data, file=open('mydata.json', 'w'))

# using the latitude and longitude above, get the weather details from another URL 
lat = json_data[0]['lat']
lon = json_data[0]['lon']

# Template request
requesturl = f"https://api.weather.gov/points/{lat},{lon}" 
weather_data = fetchdata(requesturl)

# store weather data in a file
print(weather_data, file=open('weatherdata.json', 'w'))