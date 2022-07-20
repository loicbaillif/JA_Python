#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Load Module: Exercise - Copysign ******

# Write a program that takes two float numbers, x and y, and prints x with 
# the sign of y. Use the copysign function defined in the math module.


# Standard Library imports
from math import copysign

# Local application imports
from print_title import print_title
from print_title import print_subtitle

print_title("JetBrains Academy - Python for Beginners")
print_title("Load Module - Exercise")
print_subtitle("Copysign")

x = int(input("Please enter x value:\n> "))
y = int(input("Please enter y value:\n "))
print(copysign(x, y))