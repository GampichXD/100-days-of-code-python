# API (Application Programming Interface) --> set of commands, function, protocols, and objects that programmers can use to create software pr interact with an external system

# Your program | API | External System

import requests
from datetime import datetime
My_LAT = -7.005145
MY_LONG = 110.438126

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# # data = response.json()['iss_position']['longitude']
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)
# print(response.status_code)
# if response.status_code != 200:
#     raise  Exception("Bad response from ISS API")
# if response.status_code == 404:
#     raise Exception("That resource does not exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access the data")
# Response Code --> https://www.webfx.com/web-development/glossary/http-status-codes/
# 1XX : Hold On
# 2XX : Here You Go
# 3XX : Go Away
# 4XX : You screwed up
# 5XX : I screwed up

parameters = {
    "lat" : My_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)


