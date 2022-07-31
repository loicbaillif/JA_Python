#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - Cotangent ******

# Write a program that reads an integer representing an angle (in degrees) 
# and prints its cotangent.
# Round the result to 10 decimal places.


# Global Python import
from math import cos, radians, sin

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions - Exercise: Cotangent")

def cotangent(a):
    a_rad = radians(a)
    return round(cos(a_rad) / sin(a_rad), 10)

angle_degrees = int(input())
print(cotangent(angle_degrees))


print_title("End of exercise")