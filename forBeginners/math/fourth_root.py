#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - The fourth root ******

# Write a program that prints the fourth root from a given real number.
#
# The square root function is located in the math module. 
# Try to find and apply it.
#
#  Do not round the result.


# Global Python import
from math import sqrt

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions - Exercise: The fourth root")

user_number = float(input())
print(sqrt(sqrt(user_number)))


print_title("End of exercise")