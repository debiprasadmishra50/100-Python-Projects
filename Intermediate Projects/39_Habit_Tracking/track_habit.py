import requests
from datetime import datetime as dt

TOKEN: str = "alalalkskskspwpwpw101010"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}


def habit_tracking():

    USERNAME = input("Enter a User Name(lower-case letters and numbers only): ").lower()

    # ---------------------- CREATE A NEW ACCOUNT WITH YOUR USERNAME - POST Request ---------------------- #
    pixela_endpoint = "https://pixe.la/v1/users"
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=pixela_endpoint, json=user_params)

    if not response.json()["isSuccess"]:
        print(f"{response.json()['message']} Try Again!\n")
        habit_tracking()
    elif response.json()["isSuccess"]:
        # ---------------------- CREATE A GRAPH - POST Request ---------------------- #
        print(f"User {user_params['username']} Created, Now Creating Graph")
        graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
        GRAPH_ID = "graph1"
        graph_params = {
            "id": GRAPH_ID,
            "name": input("\nWhich Habit you want to Track to: "),
            "unit": input("\nEnter appropriate unit of the quantity, for e.g, Kg, Calorie, Pages, Meter, Kilometer: "),
            "type": "float",
            "color": "sora"
        }

        response = requests.post(url=graph_endpoint, json=graph_params, headers=HEADERS)

        if response.json()["isSuccess"]:
            print(f"\nGraph Created, Now you can view the Graph at this URL: \n"
                  f"\n\t\thttps://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html")
            with open("link.txt", mode="w") as link:
                link.write(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html")

            return graph_endpoint, GRAPH_ID


def add_data(graph_endpoint, GRAPH_ID):
    # ---------------------- CREATE A PIXEL ON GRAPH - POST Request ---------------------- #

    pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
    today = dt.now()
    DATE = today.strftime("%Y%m%d")
    pixel_params = {
        "date": DATE,
        "quantity": input("\nHow much did you work on your Habit Today, Enter the amount/quantity only: "),
    }
    response = requests.post(url=pixel_endpoint, json=pixel_params, headers=HEADERS)
    if response.json()["isSuccess"]:
        print("\nData Added Successfully")
        return pixel_endpoint


def update_pixel(pixel_endpoint):
    # --------------------- UPDATE A PIXEL - PUT Request ---------------------- #
    DATE = dt(year=int(input("Please Enter Year: \n")), month=int(input("Please Enter Month(1-12): \n")),
              day=int(input("Please Enter Day: \n"))).strftime("%Y%m%d")
    update_pixel_endpoint = f"{pixel_endpoint}/{DATE}"
    update_params = {
        "quantity": input("\nHow much did you work on your Habit, Enter the amount/quantity only: "),
    }
    response = requests.put(url=update_pixel_endpoint, json=update_params, headers=HEADERS)
    if response.json()["isSuccess"]:
        print("Update Successful\n")


def delete_pixel():
    # ---------------------- DELETE A PIXEL - DELETE Request ---------------------- #
    DATE = dt(year=int(input("Please Enter Year: \n")), month=int(input("Please Enter Month(1-12): \n")),
              day=int(input("Please Enter Day: \n"))).strftime("%Y%m%d")
    delete_pixel_endpoint = f"{pixel_endpoint}/{DATE}"
    response = requests.delete(url=delete_pixel_endpoint, headers=HEADERS)
    if response.json()["isSuccess"]:
        print("Deleted Successfully\n")


with open("data.txt", mode="r") as file:
    if file.read() == "1":
        graph_endpoint, GRAPH_ID = habit_tracking()
        add_data(graph_endpoint, GRAPH_ID)
        with open("data.txt", mode="w") as file:
            file.write(f"2\n{graph_endpoint}\n{GRAPH_ID}")
            print("Come Back Tomorrow, Bye!")
    else:
        with open("data.txt", mode="r") as file:
            data = file.read().split("\n")
            pixel_endpoint = add_data(data[1], data[2])

            update_delete = True
            while update_delete:
                user_input = input("\nDo you want to Update or Delete any previous data: \n"
                      "u: Update\nd: Delete\nn: Do Nothing, Exit!: ")[0].lower()
                if user_input == "u":
                    update_pixel(pixel_endpoint)
                elif user_input == "d":
                    delete_pixel()
                else:
                    print("Bye, See you tomorrow!")
                    update_delete = False




