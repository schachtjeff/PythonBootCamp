print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip do you want to give? 10, 12. or 15? ")) / 100
people_split = int(input("How many people to split the bill? "))
total_split = ((total_bill * 1+ tip) / people_split)
total_split = round(total_split, 2)
print(f"Your total bill to split: {total_split}")
