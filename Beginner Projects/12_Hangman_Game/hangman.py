import pyfiglet
import random

# Print Banner
name = pyfiglet.figlet_format("hangman")
print(name, end="-" * 50 +"\n"+"-" * 50 +"\n")

# Add a Description
print("Hangman is a guessing game in which you've to guess an word, here it is an Animal, you've got 6 lives. Make sure you play fair and enjoy the game. All the best.")

from animal_list import list_of_animals
# Randomly Choose and animal
animal_chosen = random.choice(list_of_animals)
# print("Chosen word is "+animal_chosen)
word_length = len(animal_chosen)

# Keep track of player's lives, total live player has is 6
lives = 6

# Create the blank spaces
display = []
for _ in range(word_length):
    display.append('_')
# print(display)
print(f"{' '.join(display)}")

end_of_game = False
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    # Clear Console
    import os
    clear = lambda: os.system('cls')
    clear()
    
    # Print the banner always
    print(name, end="-" * 50 +"\n"+"-" * 50 +"\n")
    # keep the guesses in a list and tell user if they're guessing the letters again
    if guess in display:
        print("You've already guesses the letter "+guess)

    # Compare the guesses letter with letters of animal chosen and place letters in blanks
    for position in range(word_length):
        letter = animal_chosen[position]
        # print(f"Current position {position}\nCurrent letter {letter}\nGuessed letter {guess}")
        if letter == guess:
            display[position] = letter
    
    # print("\r"+display)
    print(f"{' '.join(display)}")

    # If guess is not a letter in chosen_word, reduce lives by 1
    if guess not in animal_chosen:
        print(f"\nYou guessed {guess} and that's not in the word. You lost a life.")
        lives -= 1
        print(f"You have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print(f"\nYou Lose :( :(\nThe animal was {animal_chosen}")
    
    # Check if the player has all the letters
    if "_" not in display:
        end_of_game = True
        print("You Won!!! Yippie...")
    
    from ascii_art import stages
    print(stages[lives])