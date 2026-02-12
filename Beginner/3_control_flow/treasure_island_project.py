# Treasure Island game.  Based on decision tree in the pdf.
print(r'''
***********************
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

#First decision.  Left is the correct answer to continue.
answer = input("You are in a dark room.  Type 'left' or 'right' for which direction: ")
if answer != 'left':
    print(f"You go {answer} and fall into a hole.  Game Over!")
else:
    print(f"You went {answer} and proceeded to the next room.")
    #Swim or wait.  'wait' is the correct answer.
    answer = input("The next room has all water with a trout.  Do you 'swim' or 'wait'? ")
    if answer != 'wait':
        print(f"You decide to {answer} and are attacked by the trout.  Game Over!")
    else:
        print(f"You decided to {answer} for the trout and it swam into a pipe.\n You proceeded to the next room.")
        #Decisions based on door color.
        answer = input("In the next room, you see 'Red', 'Blue', and 'Yellow' doors.   Which door do you choose? ")
        # Red door burns gamer
        if answer == 'Red':
            print("You enter the room, but it turns to be a big oven.  You burned by fire.  Game Over.")
        # Yellow door is winning.
        elif answer == 'Yellow':
            print("You enter the room and see a treasure chest full of gold.  You win!")
        # Blue door are beasts, game over.
        elif answer == 'Blue':
            print("You enter the room and eyes are staring at you in the dark.  You are eaten by wolves.  Game over!")
        else:
            print(f"You enter through the {answer} door and you start to fall into a quicksand.  Game Over!")

