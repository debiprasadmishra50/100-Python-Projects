from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import pyfiglet
logo = pyfiglet.figlet_format("Coffee Machine")
print(logo, end="-" * 80 + "\n" + "-" * 80 + "\n")

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True
while machine_on:
    options = menu.get_items()
    print("\nEnter 'off' to turn off the machine")
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        print("Have a good day! Bye.")
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


