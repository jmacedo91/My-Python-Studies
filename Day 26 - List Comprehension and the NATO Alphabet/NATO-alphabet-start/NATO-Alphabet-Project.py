# NATO Alphabet Project
# Open the CSV file and do the tasks:

# TODO 1. Create a Dictionary in this format:
# {new_key:new_value for (index, row) in dataframe.iterrows()}
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of phonetic code words from a word that the user inputs
# Enter a word: Thomas
#['Tango', 'Hotel', 'Oscar', 'Mike', 'Alfa', 'Sierra']

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word: ").upper()

nato_phonetic = [nato_alphabet[letter] for letter in user_word]
print(nato_phonetic)

