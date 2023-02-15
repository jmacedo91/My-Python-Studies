##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib
from random import randint

MY_EMAIL = "xxxxxxxxx@gmail.com"
PASSWORD = "notthistime"
PLACEHOLDER = "[NAME]"

# TODO 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")

# TODO 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)

for (index, row) in birthdays.iterrows():
    # TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if (row.month, row.day) == today:
        with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter_template:
            letter = letter_template.read()
            new_letter = letter.replace(PLACEHOLDER, row["name"])
        # TODO 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=row.email,
                                msg=f"Subject:Happy Birthday!\n\n{new_letter}")
