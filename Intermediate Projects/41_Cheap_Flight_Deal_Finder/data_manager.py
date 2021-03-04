import requests

SHEETY_ENDPOINTS = "https://api.sheety.co/8d0ca91dad4d7ac1f0f9f514a87fcc05/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = None

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINTS).json()
        self.destination_data = response["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINTS}/{city['id']}", json=new_data)

    def get_customer_emails(self):
        SHEETY_USER_ENDPOINT = "https://api.sheety.co/8d0ca91dad4d7ac1f0f9f514a87fcc05/flightDeals/users"
        response = requests.get(url=SHEETY_USER_ENDPOINT).json()
        self.customer_data = response['users']
        return self.customer_data
