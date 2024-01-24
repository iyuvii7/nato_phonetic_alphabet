import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for(index, row) in data.iterrows()}
user_word = input("Enter the word: ").upper()
code = [new_dict[letter] for letter in user_word]
print(f"NATO Phonetic code: {code}.")
