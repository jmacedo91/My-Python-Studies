# Sending Motivational Quotes on Mondays via Email
import datetime as dt
import smtplib
from random import choice

my_email = "jonathan.silvamacedo@gmail.com"
password = "notthistime"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Good Morning\n\n{choice(quotes_list)}")
