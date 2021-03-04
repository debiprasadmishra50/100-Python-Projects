#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60  # Use round(1.345,2) or f{1.234:.2f}
print("Welcome to Tip Calculator...")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip you want to give? 10, 12 or 15? "))
people = int(input("How many people you want to split the bill? "))
each_person_pay = round((bill + bill*tip/100) / people, 2) # (bill / people) * ((tip / 100)+1)
print(f"Each person will pay: {each_person_pay:.2f}$")

