#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Load Module: Exercise - Capitalize All Words ******

# Write a program that takes a string, capitalizes all words in it and then 
# prints the result. Use the capwords function from the string module.


# Standard Library imports
from string import capwords
 
# Local application imports
from print_title import print_title
from print_title import print_subtitle

print_title("Jet Brains Academy - Python for Beginners")
print_subtitle("Load Module: Exercise - Capitalize All Words")

input_string = input()
print(capwords(input_string))