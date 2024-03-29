#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - Particles ******

# Global Python library import
from math import expm1

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Load modules: Exercise - exponent x minus 1")


# Write a program that takes an integer x and prints e (a mathematical 
# constant) raised to the power of x, minus one. 
# Here's the formula: 
#   (e^x -1)
# 
# Use the function expm1() defined in the math module. 
# To do so, read its documentation carefully.

x = int(input("Please enter an integer"))
print(f"(e^x) - 1 = {expm1(x)}")


print_title("End of exercise")