from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from add_user import AddUser

print("Welcome to Debi's Cheap Flight Deal Finder...")

check_user = input("Choose from: \n\t1. New user\n\t2. Existing User\n")
if check_user not in ["1", "2"]:
    print("Invalid Input")
elif check_user == 1:
    AddUser()
elif check_user == 2:
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    sheet_data = data_manager.get_destination_data()

    for data in sheet_data:
        if data['iataCode'] == "":
            data['iataCode'] = flight_search.get_destination_code(data['city'])

            data_manager.destination_data = sheet_data
            data_manager.update_destination_code()

    # Checking for 6 months and checking flights from London
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    city_name = input("Enter City Name: ").title()
    ORIGIN_CITY_IATA = flight_search.get_destination_code(city_name)
    
    for destination in sheet_data:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination['iataCode'],
            from_time=tomorrow,
            to_time=six_month_from_today
        )

        if flight is None:
            continue

        if flight.price < destination['lowestPrice']:

            users = data_manager.get_customer_emails()
            emails = [row['email'] for row in users]
            passwords = [row['password'] for row in users]
            names = [row['firstName'] for row in users]

            # Message
            MESSAGE = f"Low price alert! Only ₹{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

            if flight.stop_overs > 0:
                MESSAGE += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            # Link
            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

            # Send SMS
            notification_manager.send_sms(message=MESSAGE)

            #  Send Email
            notification_manager.send_emails(message=MESSAGE, emails=emails, passwords=passwords, google_flight_link=link)

            print("We've sent flight deals to your email as well as your Phone,\nHappy Travelling")
