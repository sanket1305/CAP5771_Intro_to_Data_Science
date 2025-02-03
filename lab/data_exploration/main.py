import json
import urllib
import urllib.request

# set the headers for the request

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

# send the request to URL to get latitude, longitude for our desired location

url = "https://nominatim.openstreetmap.org/search.php?q=Compton%2C+California&format=json"

req = urllib.request.Request(url, headers = headers)
with urllib.request.urlopen(req) as response:
    data = response.read().decode('utf-8')
    json_data = json.loads(data)

# store the result in a json file

print(json_data, file=open('mydata.json', 'w'))

# using the latitude and longitude above, get the eweather details from another URL 

lat = json_data[0]['lat']
lon = json_data[0]['lon']

# Template request
requesturl = f"https://api.weather.gov/points/{lat},{lon}" 

req = urllib.request.Request(requesturl, headers = headers)
with urllib.request.urlopen(req) as response:
    data = response.read().decode('utf-8')
    weather_data = json.loads(data)

# store weather data in a file

print(weather_data, file=open('weatherdata.json', 'w'))