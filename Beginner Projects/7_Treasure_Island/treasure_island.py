print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Add your own Ascii Art : https://ascii.co.uk/
choice = input("You are stuck inside an Island and you came across a temple of treasure. You saw two paths on left and right. Which way you would go?\n").lower()

if choice == "left":
    # Continue the game
    choice1 = input("You saw a large pool full with Lotus. At the other end you see some doors but not sure and you think there's treasure inside. You have two choices, swim across or wait for a boat. What would you do?\"swim\" or \"wait\"\n").lower()
    if choice1 == "wait":
        # Continue
        choice2 = input("A boat arrives and takes you to the other end where you find 3 doors of red, yellow and blue color. Which door will you go in?").lower()
        if choice2 == "red":
            print("You got burned by fire and got human barbequed, Game Over!!!")
        elif choice2 == "blue":
            print("There was a beast with long teeth and chewed you and you dies, Game Over!!!")
        elif choice2 == "yellow":
            # Win
            print("Yayy!! You found the treasure, now you can buy chocolate!! You Win")
        else:
            print("You triggered the bomb, it went off, temple collapsed and you died. Game Over!!!")
    else:
        print("Inside the pool there was a Crocodile who eat you! Game Over!!!")
else:
    print("You walked into a room of Arrows and they pierce you and you bleed out and died. Game Over!!!")


