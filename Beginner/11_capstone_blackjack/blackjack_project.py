# Capstone Project: Blackjack Game
'''
House Rules:
- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards in card_deck definition
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.
'''
# imports
import ascii_art
import os
import random

# globals
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def is_want_to_play() -> bool:
    '''Ask if user wants to play a game'''
    answer = (input("Do you want to play a game of Blackjack? Type 'y' or 'n'"))
    # Need some more error handling direction
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("I don't understand what you said.  So 'n'.")
        return False
    
def is_want_another_card() -> bool:
    '''Ask if user wants another card'''
    answer = (input("Do you want another card? Type 'y' or 'n'"))
    # Need some more error handling direction
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("I don't understand what you said.  So 'n'.")
        return False


def clear_the_screen() -> None:
    """Clear the console screen"""
    # check if windows
    if os.name == 'nt':
        os.system('cls')
    # Otherwise assume POSIX
    else:
        os.system('clear')


def welcome() -> None:
    print(ascii_art.blackjack_display)

def receiveCard() -> int:
    '''Dealer gives one random card to whomever to then add to list.'''
    return random.choice(card_deck)

def initGame() -> int:
    '''Dealer hands out cards to players to initiate game'''
    user_cards = []
    comp_cards = []
    user_cards.append(receiveCard())
    comp_cards.append(receiveCard())
    user_cards.append(receiveCard())
    comp_cards.append(receiveCard())
    return user_cards, comp_cards

def addScoreInHand(the_hand: list) -> int:
    return sum(the_hand)

def isHandBlackJack(the_hand: list) -> bool:
    if sum(the_hand) == 21:
        return True
    else:
        return False
    
def isAcePresent(the_hand: list) -> bool:
    for card in the_hand:
        if card == 11:
            return True
        else:
            return False
        
def changeAceToOne(the_hand: list) -> int:
    ace_value = 11
    new_value = 1

    for index, value in enumerate(the_hand):
        if value == ace_value:
            the_hand[index] = new_value
            break
    return the_hand

def main() -> None:
    '''Main function'''
    play = is_want_to_play()
    while play:
        clear_the_screen()
        welcome()
        
        # Initiate Game
        initiateGame = True
        user_cards, comp_cards = initGame()
        print(f"User cards {user_cards}")
        print(f"Computer cards {comp_cards}")
        
        # Add the scores
        drawing = True
        winner = False
        while drawing and not winner:
            user_score = addScoreInHand(the_hand=user_cards)
            comp_score = addScoreInHand(the_hand=comp_cards)
            print(f"Your score is {user_score}")
            print(f"Computer's score is {comp_score}")
            print(f"User cards {user_cards}")

            # Anyone have BlackJacks?
            if initiateGame:
                initiateGame = False
                if isHandBlackJack(the_hand=user_cards):
                    print("You have BlackJack! You win!")
                    winner = True
                if isHandBlackJack(the_hand=comp_cards):
                    print("The computer has BlackJack!  The Computer Won!")
                    winner = True
            
            # Check if users score over 21
            if user_score > 21:
                if isAcePresent(the_hand=user_cards):
                    user_cards = changeAceToOne(the_hand=user_cards)
                    user_score = addScoreInHand(the_hand=user_cards)
                    print(f"Your new score is {user_score}")
                    if user_score > 21:
                        print(f"Score of {user_score} busted!  The Computer Won!")
                        winner = True
                else:
                    print(f"Score of {user_score} busted!  The Computer Won!")
                    winner = True
            
            # Ask for another card?
            if is_want_another_card() and not winner:
                user_cards.append(receiveCard())
            else:
                drawing = False

        # Computer's turn
        comp_drawing = True
        while comp_drawing:
            if comp_score > 21:
                    if isAcePresent(the_hand=comp_cards):
                        comp_cards = changeAceToOne(the_hand=comp_cards)
                        user_score = addScoreInHand(the_hand=comp_cards)
                        print(f"Your new score is {comp_score}")
                        if comp_score > 21:
                            print(f"Score of {comp_score} busted!  You Won!")
                            winner = True
                    else:
                        print(f"Score of {comp_score} busted!  You Won!")
                        winner = True
            if 2 <= comp_score <= 16:
                comp_cards.append(receiveCard())
                comp_score = addScoreInHand(the_hand=comp_cards)
            else:
                comp_drawing = False
        print(f"Computer cards {comp_cards}")

        if not winner:
            if comp_score > 21:
                print(f"Computer: {comp_score}, User: {user_score} You win!!!")
            elif user_score > comp_score:
                print(f"Computer: {comp_score}, User: {user_score} You win!!!")
            elif comp_score > user_score:
                print(f"Computer: {comp_score}, User: {user_score} Computer win!!!")
            elif comp_score == user_score:
                print(f"Computer: {comp_score}, User: {user_score} Game is a draw!!")
            else:
                print(f"Computer: {comp_score}, User: {user_score} Nobody won?! Something weird happened!?")


        play = is_want_to_play()

main()