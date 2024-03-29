#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - Sine and Cosine ******

# Write a program that reads a value representing an angle (in radians), 
# and prints the difference between its sine and cosine.
# Do not round the result.


# Global Python import
from math import sin, cos

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions - Exercise: Sine and Cosine")

angle = float(input("Please enter the angle value (in radians):\n> "))
print(sin(angle) - cos(angle))


print_title("End of exercise")