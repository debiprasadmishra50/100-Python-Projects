from twilio.rest import Client
import smtplib

# Twilio Credentials
ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = 'YOUR_VIRTUAL_NO'
SENDING_NUMBER = 'YOUR_TWILIO_VERIFIED_NO'

class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=SENDING_NUMBER
        )
        # print(message.sid)

    def send_emails(self, emails, passwords, message, google_flight_link):
        for i in range(0, len(emails)):
            EMAIL = emails[i]
            EMAIL_PASSWORD = passwords[i]

            if "gmail.com" in EMAIL:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=EMAIL, password=EMAIL_PASSWORD)
                    for email in emails:
                        connection.sendmail(from_addr=EMAIL,
                                            to_addrs=EMAIL,
                                    msg=f"Subject:New Low Price Alert!!\n\n{message}\n{google_flight_link}".encode('utf-8'))

            elif "yahoo" in EMAIL:
                with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=EMAIL, password=EMAIL_PASSWORD)
                    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                                        msg=f"Subject:New Low Price Alert!!\n\n{message}\n{google_flight_link}".encode('utf-8'))