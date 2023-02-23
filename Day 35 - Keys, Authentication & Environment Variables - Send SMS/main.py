import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("C:/Users/jhonn/AppData/Local/Programs/Python/Python311/EnvironmentVariables/.env.txt")

api_key = os.getenv("OPEN_WEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_phone_number = os.getenv("MY_PHONE_NUMBER")
active_number = os.getenv("TWILIO_ACTIVE_NUMBER")

forecast_3_hour_5_days = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": -23.537205,
    "lon": -46.796230,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url=forecast_3_hour_5_days, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_=active_number,
        to=my_phone_number
    )
    print(message.status)




