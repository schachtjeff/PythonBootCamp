# FileNotFound
#with open("a_file.txt") as file:
#    file.read()
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["not_existing_key"]
except FileNotFoundError:
    print("The file was not found")
    # Creates the file here
    #file = open("a_file.txt", "w")
except KeyError as error_message:
    print(f"The key {error_message} not found")
else:
    # When everything in 'try' succeeds
    content = file.read()
    print(content)
finally:
    # runs no matter what happens
    file.close()
    print("The file was closed")
    # raise your own error
    raise KeyError("stuff happened")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Height should not be greater than 3")

bmi = weight / height ** 2
print(bmi)

#KeyError
#a_dictionary = {"key": "value"}
#value = a_dictionary["not_existing_key"]

# IndexError
#fruit_list = ["apple", "banana", "cherry"]
#fruit = fruit_list[5]

#TypeError
#text = "abc"
#print(text + 5)