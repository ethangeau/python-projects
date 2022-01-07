# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd

nato_alphabet_df = pd.read_csv('nato_phonetic_alphabet.csv')
# print(nato_alphabet_df)
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}
# print(nato_alphabet_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please input a word: ")
code_words = [nato_alphabet_dict[letter] for letter in user_input.upper()]
print(code_words)

# list comprehension and dictionary comprehension format
# new_list = [new_item for item in origin_list if condition]
# new_dict = [new_key: new_value for (key, value) in origin_dict.items() if condition]
