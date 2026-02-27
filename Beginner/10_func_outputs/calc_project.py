#Calculator Project
# Overview: Calculator Program which does basic math of +, -, *, /
# More details:
# - Starts a loop
# - User input "What's the first number?: "n1
# - Display all operations in new lines.
# - User input, "Pick an operation: x"
# - User input, "What's the next number?: "n2
# - Display operation with n1 and n2, then the result
# - result becomes n1
# - User input, "Type 'y' to continue calculating with 'n1', or type 'n' to start a new calculation, or 'q' to quit."
# - if 'y', result becomes n1.
# - if 'q', exit loop and exit program.

#imports
import calc_art
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

number = calc_functions["*"](8, 4)
print(number)

def clear_the_screen() -> None:
    """Clear the console screen"""
    # check if windows
    if os.name == 'nt':
        os.system('cls')
    # Otherwise assume POSIX
    else:
        os.system('clear')

def welcome() -> None:
    # Clear the screen and welcome screen
    clear_the_screen()
    print(calc_art.calculator)

def set_n1(n1=None) -> float:
    if n1 is None:
        # User input to ask for n1
        n1 = float(input("What's the first number?: "))
    return n1

def set_n2() -> float:
    return float(input("What's the next number?: "))
    

def pick_operator() -> str:
    # user picks an operator.
    # would need some interfacing if user selected wrong
    for operator in calc_functions:
        print(f"{operator}\n")
    return input("Pick an operation: ")


def arithmatic(n1: float, n2: float, operator: str) -> float:
    #Calculate the result
    result = calc_functions[f"{operator}"](n1, n2)
    # Show your result
    print(f"{n1} {operator} {n2} = {result}")
    return result

def continue_calc_or_quit(last_result: float) -> str:
    # ask if want to continue using last result or new numbers, or quit
    answer = input(f"Type 'y' to continue calculating with {last_result}, or type 'n' to start a new calculation, or 'q' to quit.").lower()
    if answer != 'n' and answer != 'q':
        answer = 'y'
    return answer


def main() -> None:
    # Start loop
    calculating = 'n'
    result = 0.0
    while calculating != 'q':
        # Welcome Screen and handle n1
        if calculating == 'n':
            welcome()
            n1 = set_n1()
        else:
            n1 = set_n1(n1=result)
        # pick the operator
        operator = pick_operator()
        # get n2
        n2 = set_n2()
        result = arithmatic(n1=n1, n2=n2, operator=operator)
        calculating = continue_calc_or_quit(last_result=result)

main()