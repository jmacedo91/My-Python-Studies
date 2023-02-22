import requests

API_KEY = "notthistime"
forecast_3_hour_5_days = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": -23.537205,
    "lon": -46.796230,
    "appid": API_KEY,
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
    print("Bring an umbrella.")




