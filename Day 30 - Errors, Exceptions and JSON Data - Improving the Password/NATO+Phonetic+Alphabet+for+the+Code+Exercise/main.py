import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# is_done = False
# while not is_done:
# 	word = input("Enter a word: ").upper()
# 	try:
# 		output_list = [phonetic_dict[letter] for letter in word]
# 		print(output_list)
# 		is_done = True
# 	except KeyError:
# 		print("Sorry, only letters in the alphabet please.")


def generate_phonetic():
	word = input("Enter a word: ").upper()
	try:
		output_list = [phonetic_dict[letter] for letter in word]
	except KeyError:
		print("Sorry, only letters in the alphabet please.")
		generate_phonetic()
	else:
		print(output_list)

generate_phonetic()

