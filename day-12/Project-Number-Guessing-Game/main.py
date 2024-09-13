from random import randint
import art
EASY_LEVEL=10
HARD_LEVEL=5
print(art.logo)
def check_answer(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("Too high")
        return turns-1
    elif user_guess<actual_answer:
        print("Too Low")
        return turns-1
    elif user_guess==actual_answer:
        print(f"You got it! The answer was {actual_answer}")
    else:
        print("You enter wrong answer!")
def set_difficulty():
    level=input("Choose a difficulty easy or hard: ").lower()
    if level=='easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL
def game():
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. ")
    answer=randint(1,100)
    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number")

        guess=int(input("Make a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("Your turns are finished! You lose!")
            return
        elif guess!=answer:
            print("Guess again. ")
game()


