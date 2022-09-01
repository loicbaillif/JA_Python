#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - Law of Sines ******

# Global Python import
from math import radians, sin

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions - Exercise: Law of Sines")

# There is a triangle on the picture below with the following parameters:
#   - angle A and sides a and c are unknown;
#   - angle B = 35°, angle C = 105°, side b = 7.
# Find the side c using the math module. Print the answer rounded to 1 decimal place.

# Sines law: a / sin(a) = b / sin(b) = c / sin(c)
b_angle = 35
b_side = 7
c_angle = 105
sin_b = sin(radians(b_angle))
sin_c = sin(radians(c_angle))
c = b_side * sin_c / sin_b
print(round(c, 1))


print_title("End of exercise")