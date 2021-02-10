import requests
from twilio.rest import Client

parameters = {
    "lat": your_latitude,
    "lon": your_longitude,
    "exclude": "current,minutely,daily",
    "appid": "your_openweather_API_key"
}

URL = "https://api.openweathermap.org/data/2.5/onecall"
# Twilio Credentials
account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"

response = requests.get(url=URL, params=parameters)
# print(response.url)  # Print full URL
response.raise_for_status()
weather_data = response.json()
will_rain = False
"""Check in first 12 hours if it's gonna rain today. The condition id is <700 for rain"""
for _ in range(0, 12):  # 12 means search within first 12 hours
    condition_id = weather_data['hourly'][_]['weather'][0]['id']
    if condition_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)  # twilio API, sending sms
    message = client.messages \
        .create(
        body="It's going to rain today, Please take an Umbrella with you!",
        from_='your_phone_no_from_twilio',
        to='sending_number_with_country_code'
    )
    print(message.status)
    print(message.sid)


