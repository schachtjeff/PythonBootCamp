"""
Auction Program 
- Asks a user there name and a price.
- Continues asking for bidders, while clearing the screen, until no more bids.
- Then checks to find the highest bid.
"""

import os
import art_gavel as gavel

people_bidding = {}

def clear_the_screen() -> None:
    """Clear the console screen"""
    # check if windows
    if os.name == 'nt':
        os.system('cls')
    # Otherwise assume POSIX
    else:
        os.system('clear')

def welcome_message() -> None:
    print(gavel.gavel)
    print("Welcome to the secret auction program.\n")

def add_bidder() -> None:
    bid_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    people_bidding[bid_name] = bid_amount

def is_another_bidder() -> bool:
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
    if another_bidder == 'no':
        return False
    elif another_bidder == 'yes':
        return True
    else:
        return True
    
def find_highest_bid() -> None:
    highest_name = ''
    highest_value = 0
    for key, value in people_bidding.items():
        if value > highest_value:
            highest_value = value
            highest_name = key
    print(f"The winner is {highest_name} with a bid of ${highest_value}.")

def main() -> None:
    welcome_message()
    more_bidders = True
    while more_bidders != False:
        add_bidder()
        if not is_another_bidder():
            more_bidders = False
        else:
            clear_the_screen()
    find_highest_bid()

# The winner is 'somebody' with a bid of $nnn.
main()