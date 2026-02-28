#Project: Number Guessing Project
'''
Overview:
- Welcome message
- stating to guess between a high and low numbers (e.g. 1 and 100)
- User chooses difficulty easy (10 guesses) or hard (5 guesses)
- Loop starts with States how many attemtps remaining.
- User makes a number guess.
- Computer states, too high/low or correct.
- User wins if correct.
- Lose an attempt and compare if there are 0 attempts.
- User loses if at 0 attempts.
- Play again? back to welcome message if yes.
'''

# imports
import os
import random

# Globals
LOW_NUMBER = 1
HIGH_NUMBER = 100
EASY_GUESSES = 10
HARD_GUESSES = 5


def clear_the_screen() -> None:
    """Clear the console screen"""
    # check if windows
    if os.name == 'nt':
        os.system('cls')
    # Otherwise assume POSIX
    else:
        os.system('clear')

def welcome() -> None:
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {LOW_NUMBER} and {HIGH_NUMBER}.")

def randomNumberChosen() -> int:
    return random.randint(LOW_NUMBER, HIGH_NUMBER)

def chooseDifficulty() -> str:
    user_dif = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_dif == 'easy' or user_dif == 'hard':
        return user_dif
    else:
        print("I don't know what you said, so I'll give you easy.")
        return 'easy'
    
def getNumberOfAttempts(difficulty: str) -> int:
    if difficulty == 'easy':
        return EASY_GUESSES
    elif difficulty == 'hard':
        return HARD_GUESSES
    else:
        return EASY_GUESSES
    
def getGuessFromUser() -> int:
    return int(input("Make a guess: "))

def isUserCorrect(user_guess, answer) -> bool:
    if user_guess == answer:
        return True
    else:
        return False
    
def isUserGuessHigh(user_guess, answer) -> bool:
    if user_guess > answer:
        return True
    else:
        return False
    
def isUserGuessLow(user_guess, answer) -> bool:
    if user_guess < answer:
        return True
    else:
        return False
    
def is_want_to_play() -> bool:
    '''Ask if user wants to keep playing a game'''
    answer = (input("Do you want to keep playing? Type 'y' or 'n'"))
    # Need some more error handling direction
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("I don't understand what you said.  So 'n'.")
        return False

def main() -> None:
    still_playing = True
    while still_playing:
        clear_the_screen()
        welcome()
        the_answer = randomNumberChosen()
        difficulty = chooseDifficulty()
        attempts = getNumberOfAttempts(difficulty=difficulty)
        
        #Loop to keep guessing until correct or run out of guesses.
        correct_guess = False
        while attempts > 0 and not correct_guess:
            user_guess = getGuessFromUser()
            if isUserCorrect(user_guess=user_guess, answer=the_answer):
                correct_guess = True
            elif isUserGuessHigh(user_guess=user_guess, answer=the_answer):
                print("Too high.")
                attempts -= 1
                print("Guess again.")
                print(f"You have {attempts} remianing to guess the number.")
            elif isUserGuessLow(user_guess=user_guess, answer=the_answer):
                print("Too low.")
                attempts -= 1
                print("Guess again.")
                print(f"You have {attempts} remianing to guess the number.")

        if correct_guess:
            print(f"You got it! The answer was {the_answer}.")
        else:
            print(f"Sorry, you didn't get the correct number which was {the_answer}.")
        
        # Play again?
        still_playing = is_want_to_play()

main()