print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age > 18:
        bill = 12
        print("Adult tickets are $12")
    else:
        bill = 7
        print("Youth tickets are $7")
    
    answer = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if answer == "y":
        bill += 3
    print(f"Your bill is: {bill}")
else:
    print("Sorry!  You are not allowed.")