from art import logo
from replit import clear

print(logo)
# Calculator Functions

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?\n"))

    for symbol in operations:
        print(symbol)

    calculating = True
    while calculating:
        operation_symbol = input("Pick an operation from above: ")
        num2 = float(input("What's the next number?\n"))
        answer = operations[operation_symbol](num1, num2)  # Call appropriate function
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type \"y\" to calculate with {answer}, or type \"n\" to start a new calculation, \"q\" to exit the calculator: ").lower()
        if choice == "y":
            num1 = answer
        elif choice == "n":
            calculating = False
            clear()
            calculator()
        else:
            print("Good Bye!!")
            calculating = False

calculator()