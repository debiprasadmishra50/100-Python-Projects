import requests
from datetime import datetime
import base64
from prettytable import PrettyTable

APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
try:
    with open("data.txt", mode="r") as file:
        data = file.read().split("\n")
        GENDER = data[1]
        WEIGHT_KG = float(data[2])
        HEIGHT_CM = float(data[3])
        AGE = int(data[4])
except FileNotFoundError:
    with open("data.txt", mode="w") as file:
        GENDER = input("Save your data to Local Machine\nEnter your Gender: ").lower()
        WEIGHT_KG = input("Enter your Weight(Kg): ")
        HEIGHT_CM = input("Enter your height(cm): ")
        AGE = input("Enter your age: ")
        file.write(f"1\n{GENDER}\n{WEIGHT_KG}\n{HEIGHT_CM}\n{AGE}")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_workout = input("What Exercises/Workouts did you do today: ")
parameters = {
 "query": user_workout,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}
response = requests.post(url=exercise_endpoint, json=parameters, headers=HEADERS)
result = response.json()


# --------------------------- For Sheety -------------------------------- #
today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_endpoint = "https://api.sheety.co/8d0ca91dad4d7ac1f0f9f514a87fcc05/workoutTracking/workouts"

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    try:
        with open("login.txt", mode="r") as file:
            credentials = file.read()
    except FileNotFoundError:
        ID = input("\nSave Your Data in Local Machine\nEnter your username: ")
        PASS = input("Enter your Password: ")
        with open("login.txt", mode="w") as file:
            credentials = f"{ID}:{PASS}"
            file.write(base64.b64encode(credentials.encode()).decode())  # String
        with open("login.txt", mode="r") as file:
            credentials = file.read()

    password = base64.b64decode(credentials.encode()).decode().split(":")[1]
    PASS = input("\nAuthenticate Yourself before adding data\nEnter your Password: ")
    if PASS == password:
        sheety_headers = {
            "Authorization": f"Bearer {credentials}",
            "Content-Type": "application/json",
        }
        response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
        print("Data Added Successfully!")

        # ---------------- GET DATA ---------------- #
        see_records = input("\nDo you want to see your previous records(y/n): ").lower()

        if see_records.lower() == "y":
            records = requests.get(url=sheety_endpoint, headers=sheety_headers).json()
            table = PrettyTable()
            table.field_names = list(records["workouts"][0].keys())[0:5]
            for record in records["workouts"]:
                table.add_row(
                    [record['date'], record['time'], record['exercise'], record['duration'], record['calories']])
            print(table)
            print("\nBye, See you tomorrow!")
        else:
            print("\nBye, See you tomorrow!")
    else:
        print("\nWrong Password")

