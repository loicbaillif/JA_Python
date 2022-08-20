#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - The logarithmic value ******

# Global Python import
import math

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions - Exercise: The logarithmic value")

# Write a program that reads two integers (the first is always positive) 
# and calculates the logarithmic value of the first integer with the second 
# integer as a base. If the second integer is negative, 0 or 1, return the 
# natural log of the first number.
#
# Use the function log() from the math module. With one argument, it returns 
# the natural logarithm of a number. It can also take two arguments: 
# a number and a logarithmic base.
#
# Print the result rounded to 2 decimal places.

user_number = int(input())
user_base = int(input())

if user_base <= 0:
    result = math.log(user_number)
elif user_base == 1:
    result = math.log(user_number)
else:
    result = math.log(user_number, user_base)

print(round(result, 2))


print_title("End of exercise")