print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepporni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_bill = 0

#TODO: work out how much they need to pay based on their size choice.
# small pizza is $15
# medium pizza is $20
# large pizza is $25
if size == "S":
    total_bill += 15
    if pepporni == "Y":
        total_bill += 2
    if extra_cheese == "Y":
        total_bill += 1
elif size == "M":
    total_bill += 20
    if pepporni == "Y":
        total_bill += 3
    if extra_cheese == "Y":
        total_bill += 1
elif size == "L":
    total_bill += 25
    if pepporni == "Y":
        total_bill += 3
    if extra_cheese == "Y":
        total_bill += 1
else:
    print("I don't understand!")
    exit()

#TODO: work out how much to add to their bill based on their pepperoni choice.
# pepperoni for small is +$2
# pepperoni for medium or large is +$3



# TODO: work out their final amount based on whether if they want extra cheese.
# extra cheese for any size is +$1


print(f"Your total bill for the pizza is: ${total_bill}")
