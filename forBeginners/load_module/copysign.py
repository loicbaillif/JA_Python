#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Load Module: Exercise - Copysign ******

# Write a program that takes two float numbers, x and y, and prints x with 
# the sign of y. Use the copysign function defined in the math module.


# Standard Library imports

# Local application imports
from math import copysign
from print_title import print_title
from print_title import print_subtitle

print_title("JetBrains Academy - Python for Beginners")
print_title("Load Module - Exercise")
print_subtitle("Copysign")

x = int(input())
y = int(input())
print(copysign(x, y))