#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - Heron's formula ******

# Global Python import
import math

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions - Exercise: Heron's Formula")

# uses Heron's formula to return the area of a triangle, given its 3 sides 
def semi_perimeter(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


a = int(input("Please enter the length of the first side: \n> "))
b = int(input("Please enter the length of the second side: \n> "))
c = int(input("Please enter the length of the third side: \n> "))
print(semi_perimeter(a, b, c))


print_title("End of exercise")