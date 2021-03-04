from art import logo, vs
from game_data import data
import random
print(logo)

# Choose Values
value1 = random.randint(0, len(data)-1)
def choose_value2():
    value2 = random.randint(0, len(data)-1)
    while value2 == value1:
        value2 = random.randint(0, len(data))
    return value2
value2 = choose_value2()

def display_data(value1, value2):
    print(f"Compare A: {data[value1]['name']}, a {data[value1]['description']}, from {data[value1]['country']}")
    print(vs)
    print(f"Compare B: {data[value2]['name']}, a {data[value2]['description']}, from {data[value2]['country']}")

def compare_values(value1, value2, guess):
    follower_a, follower_b = data[value1]['follower_count'], data[value2]['follower_count']
    # print(follower_a, end=f" {follower_b}\n")
    def compare(follower_a, follower_b):
        if follower_a > follower_b:
            return "a"
        elif follower_b > follower_a:
            return "b"
    if guess == "b":
        return compare(follower_a, follower_b)
    elif guess == "a":
        return compare(follower_a, follower_b)


# Start the Game
score = 0
game_on = True
while game_on:
    display_data(value1, value2)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    comparison = compare_values(value1, value2, guess)
    if comparison == guess:
        value1 = value2
        value2 = choose_value2()
        # Clear Console
        import os
        clear = lambda: os.system('cls')
        clear()
        print(logo)
        score += 1
        print(f"You're right, Current score: {score}")
    else:
        # Clear Console
        import os
        clear = lambda: os.system('cls')
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_on = False
