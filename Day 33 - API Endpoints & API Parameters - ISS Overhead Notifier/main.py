import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -23.537205
MY_LONG = -46.796230
MY_EMAIL = "xxxxxxxxxxxxxxxxxx@gmail.com"
PASSWORD = "notthistime"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    lat_interval = (MY_LAT + 5) >= iss_latitude >= (MY_LAT - 5)
    long_interval = (MY_LONG + 5) >= iss_longitude >= (MY_LONG - 5)
    return lat_interval and long_interval


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    is_currently_dark = (time_now <= sunrise) or (sunset <= time_now)
    return is_currently_dark


# If the ISS is close to my current position, and it is currently dark
while True:
    if is_iss_overhead() and is_night():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Look up!\n\nThe ISS is above of you now, look up and enjoy this moment")
    time.sleep(3600)
