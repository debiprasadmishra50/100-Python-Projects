import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("Enter 0 for rock, 1 for paper and 2 for scissors. What do you choose?\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid Input, You Lose :(")
else:
    print("You Choose:"+game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer Choose {game_images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You Win :)")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose :(")
    elif user_choice > computer_choice:
        print("You Win :)")
    elif computer_choice > user_choice:
        print("You Lose :(")
    elif computer_choice == user_choice:
        print("It's a Draw")

