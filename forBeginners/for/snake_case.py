#  ******** JetBrains Academy - Python for Beginners ********
#  ****** for loop: Exercise - snake_case ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("for loop: Exercise - snake_case")


# https://hyperskill.org/learn/step/9476
# Since we are learning Python, sometimes it might be useful to convert text 
# from lowerCamelCase to snake_case. The main trick is to find the correct 
# place where to insert an underscore. Let's make a rule that an underscore 
# should be inserted right before a capital letter, so lowerCamelCase would 
# become lower_camel_case.
#
# The input format:
#   Read a word or a phrase written in lowerCamelCase
#
# The output format:
#   Print out words in lowercase and separate them by underscores.

user_phrase = input()

# Variables
phrase_in_snake_case = ""

for letter in user_phrase:
    if letter.isupper():
        phrase_in_snake_case += "_"
        phrase_in_snake_case += letter.lower()
    else: 
        phrase_in_snake_case += letter

print(phrase_in_snake_case)

print_title("End of exercise")