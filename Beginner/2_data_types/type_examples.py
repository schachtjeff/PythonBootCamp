# TypeError: expecting another type like string for len function, not integer
#print(len(12345))

# Find the data type -> class 'str'
print(type('Hello'))
# class 'int'
print(type(123))

# class 'float'
print(type(3.14))

# class 'bool'
print(type(True))

# Type conversion challenge, needed to add str to concat another string.
print("Number of letters in your name: " + str(len(input("Enter your name: "))))