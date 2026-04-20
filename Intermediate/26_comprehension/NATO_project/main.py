#Imports
import csv
import pandas as pd

# Constants
NATO_FILE = "nato_phonetic_alphabet.csv"


#1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

def read_nato_csv_to_dict(file_name) -> dict:
    with open(file_name) as csv_file:
        nato_reader = csv.reader(csv_file)
        return {letter: nato_call for (letter, nato_call) in nato_reader if len(letter) == 1}

def read_nato_csv_to_dict_pd(file_name) -> dict:
    data = pd.read_csv(file_name)
    pnonetic_dict ={row.letter: row.code for (index, row) in data.iterrows()}
    return pnonetic_dict

#2. Create a list of the phonetic code words from a word that the user inputs.
def create_phonetic_list_from_name(user_name: str, nato_dict: dict) -> list:
    return [nato_dict[letter.upper()] for letter in user_name]

def create_phonetic_list_from_name_pd(user_name: str, nato_dict: dict) -> list:
    return [nato_dict[letter.upper()] for letter in user_name]

# Main file
#nato_dict =  read_nato_csv_to_dict(NATO_FILE)
nato_dict = read_nato_csv_to_dict_pd(NATO_FILE)
#print(nato_dict)
user_input = True
while user_input:
    user_name = input("Enter your name to change for NATO phonetic alphabet: ")
    #phonetic_list = create_phonetic_list_from_name(user_name, nato_dict)
    phonetic_list = create_phonetic_list_from_name_pd(user_name, nato_dict)
    print(phonetic_list)
    # Get phonetic name
    user_choice = input("Would you like to try again? (y/n): ")
    if user_choice.lower() == "n":
        user_input = False




