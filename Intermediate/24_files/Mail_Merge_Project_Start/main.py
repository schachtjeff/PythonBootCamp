#Instructions
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Constant
PLACEHOLDER = "[name]"

with open("./Input/Names/names.txt", 'r') as names_file:
    names_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", 'r') as letter_file:
    letter_contents = letter_file.read()
    for name in names_list:
        new_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, new_name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt") as completed_letter:
            completed_letter.write(new_letter)


