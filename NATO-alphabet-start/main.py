import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass


nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabets_dict = {row.letter: row.code for (index, row) in nato_alphabets.iterrows()}
# {"A": "Alfa", "B": "Bravo"}

while True:
    user_input = input("Input a word: ")
    try:
        result = [nato_alphabets_dict[letter] for letter in user_input.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet")
    else:
        print(result)
        break
