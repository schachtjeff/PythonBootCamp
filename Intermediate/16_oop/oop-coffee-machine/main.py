from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main() -> None:
    coffee_menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()

    # Loop until user types 'off'
    off = False
    while not off:
        options = coffee_menu.get_items()
        user_answer = input(f"What would you like? ({options}): ").lower()
        if user_answer == 'espresso' or user_answer == 'latte' or user_answer == 'cappuccino':
            drink = coffee_menu.find_drink(user_answer)
            if coffee_machine.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
        elif user_answer == 'report':
            coffee_machine.report()
            money_machine.report()
        elif user_answer == 'off':
            off = True
            print("Goodbye!")
        else:
            print(f"I don't understand what you mean by, '{user_answer}'")

main()
