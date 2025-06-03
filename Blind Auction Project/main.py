# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
print("Welcome to the bid!")
play_again = True
bidders = {}
winner_bid = 0
winner = ""


while play_again:
    name = input("What is your name: ")
    bid = int(input("How much would you like to bid: "))
    bidders[name] = bid
    more_bidders = input("Are there any more bidders: Type 'yes' if there are more bidders and 'no' if there are no more bidders: ").lower()
    if more_bidders == "yes":
        print("\n" * 100)
        play_again = True
    else:
        play_again = False

for name in bidders:
    if bidders[name] > winner_bid:
        winner = name
        winner_bid = bidders[name]

print(f"The bid winner is {winner} with a bid of {winner_bid}")



# print(bidders)

