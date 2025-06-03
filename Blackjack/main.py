import art
import random

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_play = True
player_card = []
computer_card = []

def player_drawing_card():
    card = random.choice(cards)
    player_card.append(card)
    return card

def computer_drawing_card():
    card = random.choice(cards)
    computer_card.append(card)
    return card

def start():
    player_drawing_card()
    player_drawing_card()
    first_computer_card = computer_drawing_card()
    computer_drawing_card()
    print(f"Your cards: {player_card}, current score: {sum(player_card)}")
    print(f"Computer's first card: {first_computer_card}")

def another_player_card():
    player_drawing_card()
    while sum(player_card) > 21 and 11 in player_card:
        index = player_card.index(11)
        player_card[index] = 1
    print(f"Your cards: {player_card}, current score: {sum(player_card)}")
    print(f"Computer's first card: {computer_card[0]}")

def yes_or_no():
    another_card = input("Type yes for another card or type no if you want to pass: ")
    if another_card == "yes":
        another_player_card()
        if sum(player_card) > 21:
            print("YOU LOST :( - YOUR CARD SUM IS > 21")
            return False
        return True
    else:
        print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
        return None

def compare():
    if sum(player_card) > sum(computer_card):
        print("YOU WIN :D")
    elif sum(computer_card) > 21:
        print("Computer went bust. You win")

    elif sum(player_card) == sum(computer_card):
        print("YOU TIED")
    else:
        print("YOU LOST :(")

play = input("Do you want to play Blackjack - type yes or no: ")
if play == "yes":
    start()
    while continue_play:
        continue_play = yes_or_no()
        while sum(computer_card) < 17:
            computer_drawing_card()
    print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
    if not sum(player_card) > 21:
        compare()
else:
    print("Have a good day!")






