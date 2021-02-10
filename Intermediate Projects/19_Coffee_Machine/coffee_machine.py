from Menu import resources, MENU
import pyfiglet
logo = pyfiglet.figlet_format("Coffee Machine")
print(logo, end="-" * 80 + "\n" + "-" * 80 + "\n")


def calculate_money(choice):
    print("Please Insert Coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_amount = 0.01 * pennies + 0.10 * dimes + 0.05 * nickles + 0.25 * quarters

    if total_amount >= MENU[choice]["cost"]:
        print(f"Here is your ${total_amount - MENU[choice]['cost']:.2f} in change")
        resources["money"] += MENU[choice]["cost"]
        for item in MENU[choice]["ingredients"]:
            resources[item] -= MENU[choice]["ingredients"][item]
        return True
    else:
        print("Sorry, that's not enough money. Money Refunded")


def check_ingredients(choice):
    for item in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][item] >= resources[item]:
            print(f"Sorry, Not enough {item}")
            return False
    return calculate_money(choice)


def print_report():
    for item in resources:
        if item == "water":
            print(f"Water: {resources[item]}ml")
        elif item == "milk":
            print(f"Milk: {resources[item]}ml")
        elif item == "coffee":
            print(f"Coffee: {resources[item]}gm")
        elif item == "money":
            print(f"Money: ${resources[item]}")


def coffee_machine():
    machine_on = True
    while machine_on:
        print("\nEnter 'report' to check the machine content status.")
        choice = input("What would you like? (espresso/latte/cappuccino)\nType 'cancel' to quit: ").lower()

        if choice == "report":
            print_report()
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            if check_ingredients(choice):
                print(f"Here is your {choice} ☕. Enjoy!")
        elif choice == "cancel":
            print("Have a good day! Bye.")
            machine_on = False
        else:
            print("Please Enter a Valid Choice")


print("Welcome to Coffee Machine.")
coffee_machine()

