programming_dictionary = {
    "Bug": "An error in a program that prevents the program for functioning as intended.", 
    "Function": "A piece of code you can call over and over again.",
    "Loop": "The action of doing something over and over again."}

# to get 'bug's value'
print(programming_dictionary["Bug"])

# to add another item into the dictionary
programming_dictionary["stuff"] = "there are new things here"
print(programming_dictionary)

# to wipe an existing directory
#programming_dictionary = {}

# edit an item in the dictionary, same as adding
programming_dictionary["stuff"] = "this is much newer"
print(programming_dictionary)

# Loop through a dictionary and print the value, not the key
for key in programming_dictionary:
    print(programming_dictionary[key])

# An example dictionary
colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

