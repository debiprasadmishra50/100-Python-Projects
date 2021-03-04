import pandas
import smtplib
import datetime as dt
from random import randint

MAIL = "YOUR_EMAIL@MAIL.com"
APP_PASSWORD = "YOUR_PASSWORD"

today = dt.datetime.today()
today_values = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_values in birthday_dict:
    birthday_person = birthday_dict[today_values]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_path) as file:
        letter = file.read().replace("[NAME]", birthday_person["name"])

    if "yahoo" in MAIL:
        with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MAIL, password=APP_PASSWORD)
            connection.sendmail(from_addr=MAIL, to_addrs=birthday_person["email"],
                                msg=f"Subject:Birthday Wish\n\n{letter}")
    elif "gmail" in MAIL:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MAIL, password=APP_PASSWORD)
            connection.sendmail(from_addr=MAIL, to_addrs=birthday_person["email"],
                                msg=f"Subject:Birthday Wish\n\n{letter}")




