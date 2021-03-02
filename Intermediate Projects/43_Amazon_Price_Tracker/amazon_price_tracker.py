from bs4 import BeautifulSoup
import lxml
import smtplib
import requests
from email.mime.text import MIMEText
from email.header import Header

HEADERS = {
    "User-Agent": "YOUR_USER_AGENT",
    "Accept-Language": "YOUR_ACCEPTED_LANGUAGE"
}

# -------------------- Credentials -------------------- #
try:
    with open("credentials.txt", mode="r") as file:
        data = file.readlines()
        MAIL = data[0]
        MAIL_PASSWORD = data[1]
        URL = data[2]
        BUY_PRICE = data[3]
except FileNotFoundError:
    with open("credentials.txt", mode="w") as file:
        MAIL = input("Enter your mail: ")
        MAIL_PASSWORD = input("Enter your password: ")
        URL = input("Enter the URL of the product: ")
        BUY_PRICE = float(input("Enter your buy price: "))
        file.write(f"{MAIL}\n{MAIL_PASSWORD}\n{URL}\n{BUY_PRICE}")
    with open("credentials.txt", mode="r") as file:
        data = file.readlines()
        MAIL = data[0]
        MAIL_PASSWORD = data[1]
        URL = data[2]
        BUY_PRICE = data[3]

# ----------------------- Get Price -------------------- #
response = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(response.text, 'lxml')

value = soup.find(name="span", id="priceblock_ourprice").getText()
price = float(value.split("₹")[1])
title = soup.find(name="span", id="productTitle").getText().strip()

# ---------------- Sending UTF-8 Mail -------------------- #
if price < float(BUY_PRICE):
    message = f"{title} is now {value}.\n\nBuy it from:\n{URL}"

    MESSAGE = MIMEText(message, 'plain', 'utf-8')
    subject = "Amazon Price Alert!!"
    MESSAGE['From'] = MAIL
    MESSAGE['To'] = MAIL
    MESSAGE['Subject'] = Header(subject, 'utf-8')

    if "@gmail.com" in MAIL:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MAIL, password=MAIL_PASSWORD)
            try:
                connection.sendmail(from_addr=MAIL, to_addrs=MAIL,
                                msg=MESSAGE.as_string())
            except:
                print("Mail Sending Unsuccessful")
    elif "@yahoo" in MAIL:
        with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MAIL, password=MAIL_PASSWORD)
            try:
                connection.sendmail(from_addr=MAIL, to_addrs=MAIL,
                                msg=MESSAGE.as_string())
            except:
                print("Mail Sending Unsuccessful")
