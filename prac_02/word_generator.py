"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

word_format = ""
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
number_of_letters = int(input("Enter number of letters in word: "))
# for i in range(number_of_letters):
#     letter_type = str(input("Enter c for consonant, or v for vowell: ").lower())
#     if letter_type == "c" or letter_type == "v":
#         word_format += letter_type
#     else:
#         letter_type = str(input("Enter c for consonant, or v for vowell: ").lower())

# for i in range(number_of_letters):
#     letter_entered = str(input("Enter letter or # for random vowel, or % for random consonant: ").lower())
#     if letter_entered in CONSONANTS or letter_entered in VOWELS or letter_entered == "#" or letter_entered == "%":
#         word_format += letter_entered
#     else:
#         letter_entered = str(input("Enter letter or # for random vowel, or % for random consonant: ").lower())



# word_format = "ccvcvvc"
word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    else:
        word += kind

print(word)


def is_valid_format(word):
    for letter in word:
        if letter != "c" or letter != "v":
            return False
    return True
