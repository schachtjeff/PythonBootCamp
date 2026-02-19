import random
# Password Generator Project
# Easy Version - Generate the password in sequence. Letters, then symbols
#    then numbers.  If the user wants 4 letters 2 symbols and 3 numbers
#   then the password might look like this: fgdx$*924

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
           'x', 'y', 'z', 'A', 'B', 'C', 'D', 'D', 'F', 'G', 'H', 
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
           'T', 'U', 'V', 'W', 'w', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Easy level
user_password = []
for letter in range(0, nr_letters):
    user_password.append(random.choice(letters))
for symbol in range(0, nr_symbols):
    user_password.append(random.choice(symbols))
for number in range(0, nr_numbers):
    user_password.append(random.choice(numbers))

print(f"Easy level: {user_password}")

# Hard level
random.shuffle(user_password)
#Shuffled
print(user_password)

password = ""
for item in user_password:
    password += item
print(password)
