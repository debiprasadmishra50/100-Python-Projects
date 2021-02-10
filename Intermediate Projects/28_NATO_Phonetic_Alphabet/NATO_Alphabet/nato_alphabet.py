import pandas

data_df = pandas.read_csv("nato_phonetic_alphabet.csv")  # Read the csv file

# Create a dictionary in letter:word format
nato_dict = {row.letter: row.code for (index, row) in data_df.iterrows()}

def generate_phonetic():
    # Ask the Name
    word = input("Enter the word: ").upper()

    # Create a list of phonetic words
    try:
        phonetics = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the word please!")
        generate_phonetic()
    else:
        print(phonetics)


generate_phonetic()
