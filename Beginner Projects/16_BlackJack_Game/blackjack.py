from art import logo
import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the sum of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents as blackjack
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!!\n"
    elif computer_score == 0:
        return "You Lose, Computer has a BlackJack\n"
    elif user_score == 0:
        return "You win, You have a BlackJack\n"
    elif user_score > 21:
        return "You went over 21, you lose.\n"
    elif computer_score > 21:
        return "Computer Went Over 21, You Win.\n"
    elif user_score > computer_score:
        return "You Win :):)\n"
    else:
        return "You Lose :(:(\n"

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    # Deal cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Start the game
    while not game_over:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your Cards:  {user_cards}, current score = {user_score}")
        print(f"   Computer's First Card:  {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type \"y\" to get another card, type \"n\" to pass: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score  < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards} and the final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards} and the final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you wanna play Blackjack? Type 'y' for yes and 'n' to pass: ") == "y":
    # Clear Console
    import os
    clear = lambda: os.system('cls')
    clear()
    play_game()
