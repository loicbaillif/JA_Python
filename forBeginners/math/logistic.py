#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - Logistic functions ******

# Global Python import
from math import exp

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions: Exercise - Logistic functions")

# https://hyperskill.org/learn/step/6348
# Write a program that reads an integer and calculates the value of its 
# logistic function. A logistic function, or sigmoid function, is a function 
# defined by the formula 
#   sigma(x) = 1 / (1 + e^(-x)) = e^x / (e^x + 1)
#
# Print the result rounded to 2 decimal places.

user_input = int(input("Please enter an integer:\n> "))
logistic_user_input = exp(user_input) / (exp(user_input) + 1)
print(f"sigma({user_input}) = {round(logistic_user_input, 2)}")


print_title("End of exercise")