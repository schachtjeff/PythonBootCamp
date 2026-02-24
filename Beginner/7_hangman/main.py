import random
word_list = ["aardvark", "baboon", "camel"]
total_lives = 6

# Functions
def generate_random_word() -> str:
    return random.choice(word_list)

def generate_blanks_in_word(the_word) -> str:
    blanks = []
    for char in the_word:
        blanks.append("_")
    return blanks

def print_array_chars_to_strings(this_array):
    result_string = ''
    for char in this_array:
        result_string += char
    print(result_string)

def is_letter_guessed_in_word(this_array, guessed_letter) -> bool:
    for char in this_array:
        if char == guessed_letter:
            print(f"The {guessed_letter} is in the word.")
            return True
    return False

def replace_blanks_with_found_letters(the_word, guessed_letter, blanks) -> str:
    word_place = 0
    for char in the_word:
        if char == guessed_letter:
            blanks[word_place] = guessed_letter
        word_place += 1
    return blanks

def is_blanks_all_gone(user_word):
    for char in user_word:
        if char == "_":
            return False
    return True

#Start
print("Welcome to the Hangman game!")

#Generate a random word.
rando_word = generate_random_word()
#print(rando_word)

#Generate as many blanks as letters in word
blanks = generate_blanks_in_word(rando_word)
print_array_chars_to_strings(blanks)

# Loop
while total_lives != 0:
    print("\n#####################\n")
    print(f"You have {total_lives} lives left.\n")
    print("Mystery word: ")
    print_array_chars_to_strings(blanks)
    #Ask the user to guess a letter.
    user_letter = input("What letter will you be guessing: ").lower()
    if is_letter_guessed_in_word(this_array=rando_word, guessed_letter=user_letter):
        blanks = replace_blanks_with_found_letters(the_word=rando_word, guessed_letter=user_letter, blanks=blanks)
        # Check if all characters are full, no blanks
        if is_blanks_all_gone(user_word=blanks):
            print("You win!")
            print("Mystery word: ")
            print_array_chars_to_strings(blanks)
            break
    else:
        total_lives -= 1
        if total_lives == 0:
            print("You have no lives left.")

print("Game Over!")

