import random
from art import logo
print(logo)

def set_difficulty():
    choice = input("Choose the difficulty: Type 'easy' or 'hard': ").lower()
    if choice == "easy":
        return 10
    elif choice == "hard":
        return 5
    else:
        print("Enter a valid number")

def compare(guessed_no, random_number, attempts):
    if guessed_no > random_number:
        print("Too High.\nGuess Again")
        return attempts - 1
    elif guessed_no < random_number:
        print("Too Low\nGuess Again")
        return attempts - 1
    else:
        print(f"You guessed right, the answer was {guessed_no}")

def game():
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(0, 100)
    # print(answer)

    attempts = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts left to make the guess.")
        guess = int(input("Make a Guess: "))
        attempts = compare(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose!")
            return

game()

