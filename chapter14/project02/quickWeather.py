'''
Checking the weather seems fairly trivial: Open your web browser, click the
address bar, type the URL to a weather website (or search for one and then
click the link), wait for the page to load, look past all the ads, and so on.
Actually, there are a lot of boring steps you could skip if you had a program
that downloaded the weather forecast for the next few days and printed
it as plaintext. This program uses the requests module from Chapter
11 to
download data from the Web.
'''

import json, requests, sys

# print(len(sys.argv))
# print(sys.argv[:])
# print(sys.argv[0])
# print(sys.argv[1:])

# Step 1: Get Location from the Command Line Argument
# Compute location from command line arguments.
if len(sys.argv) < 2:
	print('Usage: quickweather.py location.')
	sys.exit()
location = ''.join(sys.argv[1:])

#Step 2: Download the JSON Data
# Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# Step 3: Load JSON Data and Print Weather
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather description
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

# When this program is run with the command line argument
# quickWeather.py San Francisco, CA, the output looks something like this:
