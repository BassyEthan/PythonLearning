import art
import random
answer = random.randint(1, 100)
lives = 0

def guessing():
    global lives
    guess = int(input("Make a guess: "))
    if guess > answer:
        print("Too high")
        print("Guess again")
        lives -= 1
        print(f"You have {lives} lives left")
    elif guess < answer:
        print("Too low")
        print("Guess again")
        lives -= 1
        print(f"You have {lives} lives left")
    else:
        print(f"You got it! The answer was {guess}")
        lives = 0



difficulty = input("Choose easy or hard: ")
if difficulty == "easy":
    lives = 10
else:
    lives = 5
while lives > 0:
    guessing()