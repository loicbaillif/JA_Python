#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - Area of a Circle ******

# Global Python import
from math import pi

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions - Exercise: Area of a circle")

# Write a program that reads an integer that represents the radius of a given 
# circle and calculates its area. To calculate the area of a circle, 
# use the following formula: 
#       S= pi * r²
# Print the result rounded to 2 decimal places.


def circle_area_from_radius(radius):
    return pi * radius * radius


print(round(circle_area_from_radius(int(input())), 2))

print_title("End of exercise")