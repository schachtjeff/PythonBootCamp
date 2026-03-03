# Coffee Machine Project
# Project Requirments download can be found below:
#  https://att-c.udemycdn.com/2020-11-10_10-05-10-450b82c80c408a663d35e3bd60526b24/original.pdf?response-content-disposition=attachment%3B+filename%3DCoffee%2BMachine%2BProgram%2BRequirements.pdf&Expires=1772569985&Signature=Whz4RkdCGChNRQmW~fq7XW48bCUC8Myq9mTd-Hg9gPd~owEx3ERa9QF3x-5ryxjYcB1CAoqd44rxWI8NBRKWIaaSREPYh1KORQ-YGG8YypkLK2mxOX~VeaqnIFDw6EK7n6tpdOkLabq-HUU~k4nW79YtAkRWJ3WdgzQwrBedjqQa8t0NpUW~5E~BY6MdmaQdcRzYf976~00IJoq~rza8vG-qoJf4WiOaYKA~Z0iylDpIMgCZDWb7ES~2~Un12AFBm2UcUVphNXwLKomrJrDX53ePA60a19xto774JoisKzNVPHRAd2l6NAoJvXd-BievC8wGI9lpa61RFRbAhOLA0A__&Key-Pair-Id=K3MG148K9RIRF4

#imports
import os
import sys

# Global
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def clear_the_screen() -> None:
    """Clear the console screen"""
    # check if windows
    if os.name == 'nt':
        os.system('cls')
    # Otherwise assume POSIX
    else:
        os.system('clear')

def makeCoffee() -> None:
    pass

def printReport() -> None:
    pass

def main() -> None:
    # Loop until user types 'off'
    off = False
    while not off:
        user_answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_answer == 'espresso':
            makeCoffee()
        elif user_answer == 'latte':
            makeCoffee()
        elif user_answer == 'cappuccino':
            makeCoffee()
        elif user_answer == 'report':
            printReport()
        elif user_answer == 'off':
            off = True
            print("Goodbye!")
        else:
            print(f"I don't understand what you mean by, '{user_answer}'")

main()