import pyfiglet
logo = pyfiglet.figlet_format("Caesar\nCipher")
print(logo, end="-"*50+"\n"+"-"*50+"\n\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function
def ceaser(direction, text, shift):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet: 
            end_text += alphabet[alphabet.index(char) + shift]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")


go_again = True
while go_again:

    # Taking Input
    ok = False
    while not ok:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ["encode", "decode"]:
            print("Please choose between \"encode\" and \"decode\"")
        else:
            ok = True
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    # Function Call
    ceaser(direction=direction, text=text, shift=shift)  

    choice = input("Enter \"yes\" to encode or decode again...Otherwise enter \"no\"\n").lower()
    if choice[0] != "y":
        print("Good Bye!!")
        go_again = False
    


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         cipher_text += alphabet[alphabet.index(letter) + shift_amount]
#     print(f"The Cipher text is: {cipher_text}")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         plain_text += alphabet[alphabet.index(letter) - shift_amount]
#     print(f"The Decoded text is: {plain_text}")

# if direction.lower() == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction.lower() == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Please enter a valid input, encode/decode")