import requests

SHEETY_ENDPOINT = "https://api.sheety.co/8d0ca91dad4d7ac1f0f9f514a87fcc05/flightDeals/users"

class AddUser:

    def __init__(self):
        self.first_name = input("Enter your First Name: ")
        self.last_name = input("Enter your Last Name: ")
        self.email = input("Enter your Email: ")
        self.password = input("Enter your password: ")
        self.add_user()

    def add_user(self):
        check_email = input("Type your email again: ")
        if self.email == check_email:

            SHEETY_PARAMS = {
                "user": {
                    "firstName": self.first_name,
                    "lastName": self.last_name,
                    "email": self.email,
                    "password": self.password
                }
            }
            response = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_PARAMS)
            print("\nCongratulations! You're in the club now")

