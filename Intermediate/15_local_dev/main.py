# Coffee Machine Project
# Project Requirments download can be found below:
#  https://att-c.udemycdn.com/2020-11-10_10-05-10-450b82c80c408a663d35e3bd60526b24/original.pdf?response-content-disposition=attachment%3B+filename%3DCoffee%2BMachine%2BProgram%2BRequirements.pdf&Expires=1772569985&Signature=Whz4RkdCGChNRQmW~fq7XW48bCUC8Myq9mTd-Hg9gPd~owEx3ERa9QF3x-5ryxjYcB1CAoqd44rxWI8NBRKWIaaSREPYh1KORQ-YGG8YypkLK2mxOX~VeaqnIFDw6EK7n6tpdOkLabq-HUU~k4nW79YtAkRWJ3WdgzQwrBedjqQa8t0NpUW~5E~BY6MdmaQdcRzYf976~00IJoq~rza8vG-qoJf4WiOaYKA~Z0iylDpIMgCZDWb7ES~2~Un12AFBm2UcUVphNXwLKomrJrDX53ePA60a19xto774JoisKzNVPHRAd2l6NAoJvXd-BievC8wGI9lpa61RFRbAhOLA0A__&Key-Pair-Id=K3MG148K9RIRF4

#imports
import os

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


def isEnoughResources(resources, coffee_name) -> bool:
    for key, value_1 in MENU[coffee_name]["ingredients"].items():
        if key in resources:
            value_2 = resources[key]
            if value_2 < value_1:
                print(f"Sorry there is not enough {key}.")
                return False
    return True


def getCoffeeCost(coffee_name: str) -> float:
    return MENU[coffee_name]["cost"]


def calculateInsertedCoins(inserted_coins) -> float:
    coinage = {
        "quaters": 0.25,
        "dimes": 0.1,
        "nickles": 0.05,
        "pennies": 0.01
    }

    total_value = 0.0

    for key, value in inserted_coins.items():
        if key in coinage:
            this_value = value * coinage[key]
            total_value += this_value
    return total_value


def askInsertCoins():
    inserted_coins = {
        "quaters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }

    for key, value in inserted_coins.items():
        inserted_coins[key] = int(input(f"How many {key}?: "))
    return inserted_coins


def isProcessCoins(coffee_name: str) -> bool:
    coffee_cost = getCoffeeCost(coffee_name=coffee_name)
    inserted_coins = askInsertCoins()
    inserted_value_coins = calculateInsertedCoins(inserted_coins=inserted_coins)
    if coffee_cost > inserted_value_coins:
        print("Sorry that's not enough money.  Money refunded.")
        return False
    else:
        change = inserted_value_coins - coffee_cost
        print(f"Here is ${round(change, 2)} in change.")
        return True


def makeCoffee(coffee_name: str, resources):
    # Make coffee with removing current resources
    for key, value_1 in MENU[coffee_name]["ingredients"].items():
        if key in resources:
            resources[key] -= value_1
    return resources


def printReport(money, resources) -> None:
    # Print resources dictionary in title
    for key, value in resources.items():
        if key == "coffee":
            print(f"{key.title()}: {value}g")
        else:
            print(f"{key.title()}: {value}ml")
    print(f"Money: ${money}")


def main() -> None:
    current_money = 0.0
    updated_resources = RESOURCES
    # Loop until user types 'off'
    off = False
    while not off:
        user_answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_answer == 'espresso' or user_answer == 'latte' or user_answer == 'cappuccino':
            if isEnoughResources(resources=updated_resources, coffee_name=user_answer):
                if isProcessCoins(coffee_name=user_answer):
                    current_money += getCoffeeCost(coffee_name=user_answer)
                    updated_resources = makeCoffee(coffee_name=user_answer, resources=updated_resources)
        elif user_answer == 'report':
            printReport(money=current_money, resources=updated_resources)
        elif user_answer == 'off':
            off = True
            print("Goodbye!")
        else:
            print(f"I don't understand what you mean by, '{user_answer}'")

main()