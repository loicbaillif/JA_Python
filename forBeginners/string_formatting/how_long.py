#  ******** JetBrains Academy - Python for Beginners ********
#  ****** String Formatting: Exercise - How long is that word? ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("String Formatting: Exercise - How long is that word?")


# https://hyperskill.org/learn/step/6896
# Write a program that calculates the length of a word from the input and 
# prints it out together with the word in the format *word* has *N* letters. 
# There will always be more than one letter in the word.

user_word = input()
word_length = len(user_word)
print(f"{user_word} has {word_length} letters")

print_title("End of exercise")