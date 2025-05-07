import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_key = "957c6fcebd6d8a592e4f665dccb662b5"
account_sid = "ACb45f5707162681ec37296bf3be98a89d"
auth_token = "5f84a8d10cd66529e290daeb69b4b9b6"
# account_sid = os.environ["ACb45f5707162681ec37296bf3be98a89d"]
# auth_token = os.environ["5f84a8d10cd66529e290daeb69b4b9b6"]

# lat = -7.005145
# lon = 110.438126
#Angela's way
weather_params = {
    'lat' : -7.005145,
    'lon' : 110.438126,
    'appid': API_key,
    'cnt':4,
}


# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}")
response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
# print(weather_data['list'][0]['weather'][0]['id'])

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="Its going to rain today. Remember to bring an ☂️",
    #     from_="+15024011312",
    #     to="+6282320835440",
    # )
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella ☂️",
        to="whatsapp:+6282320835440"
    )
    print(message.body)









