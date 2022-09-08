#  ******** JetBrains Academy - Python for Beginners ********
#  ****** for loop: Exercise - Vowels count ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("for loop: Exercise - Vowels count")


# https://hyperskill.org/learn/step/7199
# You have a predefined string vowels that contains all letters designating 
# vowel sounds. Write a program that counts the number of vowels in the 
# variable string and prints this number.

vowels = "aeiou"  # 'y' not considered as a vowel in english
user_string = input()
nb_vowels = 0

for letter in user_string:
    nb_vowels += letter in vowels

print(nb_vowels)

print_title("End of exercise")