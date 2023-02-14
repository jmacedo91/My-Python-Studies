# import smtplib
#
# my_email = "jonathan.silvamacedo@gmail.com"
# password = "notthistime"
#
# # 1️⃣ Creating Connection
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # SMTP Information
#     # Gmail = smtp.gmail.com
#     # Hotmail = smtp.live.com
#     # Yahoo = smtp.mail.yahoo.com
#
#     # 2️⃣ Init the TLS (Transport Layer Security)
#     connection.starttls()
#
#     # 3️⃣ Login
#     connection.login(user=my_email, password=password)
#
#     # 4️⃣ Send Email
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="jonathanmacedo91@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")
#
# # 5️⃣ Closing Connection
# # connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(now)
print(year)
print(month)
print(day_of_week)

if year == 2023:
    print("Wear a face mask")

date_of_birth = dt.datetime(year=1992, month=8, day=30, hour=4)
print(date_of_birth)