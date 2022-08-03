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


def fourth_root(x):
    if (x >= 0):
        return sqrt(sqrt(x))
    else:
        return "no real solution"


user_number = float(input("Please enter a float number"))
print(fourth_root(user_number))


print_title("End of exercise")