print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is you age? "))
bill = 0

if height >= 120:
    print("You can go in...")
    if age < 12:
        print("Please pay $5.00")
        bill = 5
    elif age > 12 and age <= 18:
        print("Please pay $7.00")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is gonna be ok. Have a free ride on us!")
    else:
        print("Please pay $12.00")
        bill = 12
        
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == 'Y':
        print("Please pay $3.00")
        bill += 3
    
    print(f"Your final bill is {bill}$")
else:
    print("Sorry, Come back later.")
    