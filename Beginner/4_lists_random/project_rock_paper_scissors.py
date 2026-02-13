import random

#Credits:
#- RPS Hands by Veronica Karlsson, https://www.asciiart.eu/people/body-parts/hand-gestures

rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = r'''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
'''
scissors = r'''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
'''
game_options = [rock, paper, scissors]
user_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(user_num)
if user_num < 0 or user_num > 3:
    print("ERROR! You choose something weird!")
else:
    user_choice = game_options[user_num]
    print(user_choice)
    computer_choice = random.choice(game_options)
    print("Computer choose: ")
    print(computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!!")
    elif user_choice == rock and computer_choice == paper:
        print("The Computer Wins!!")
    elif computer_choice == rock and user_choice == paper:
        print("You Win!!")
    elif computer_choice == rock and user_choice == scissors:
        print("The Computer Wins!!")
    elif computer_choice == paper and user_choice == scissors:
        print("You Win!!")
    elif user_choice == rock and computer_choice == scissors:
        print("You Win!!")
    elif computer_choice == scissors and user_choice == paper:
        print("The Computer Wins!!")