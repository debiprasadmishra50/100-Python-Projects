from art import logo
print(logo)

def highest_bidder(bidding_record):
    result = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > result:
            result = bidding_record[bidder]
            winner = bidder
    print(f"The highest bidder is {winner} and the bidding amount is {result}$.")


bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))
    bids[name] = price
    choice = input("Are there any other bidders? Type \"yes\" or \"no\"\n").lower()
    if choice == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif choice == "yes":
        # Clear Console
        import os
        clear = lambda: os.system('cls')
        clear()


