"""
If the ISS is close to my location and it is night time, then send me email to tell me to look up.
Run the code every 60 secs
"""
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = "Your Latitude"  # My Latitude
MY_LON = "Your Longitude"  # My longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # print(iss_longitude, iss_latitude)

    # My position within +5 or -5 degrees of the ISS Position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LON-5 <= iss_longitude <= MY_LON+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        MAIL = "your_email@mail.com"
        APP_PASSWORD = "your_password"

        if "yahoo" in MAIL:
            with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MAIL, password=APP_PASSWORD)
                connection.sendmail(from_addr=MAIL, to_addrs=MAIL,
                                    msg="Subject:ISS Overhead\n\nLook up, ISS is overhead.")
        elif "gmail" in MAIL:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MAIL, password=APP_PASSWORD)
                connection.sendmail(from_addr=MAIL, to_addrs=MAIL,
                                    msg="Subject:ISS Overhead\n\nLook up, ISS is overhead.")
