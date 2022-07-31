#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Theory ******

# Global Python import
import math

# Local application imports
from print_title import print_title
from print_title import print_subtitle

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions")

print_subtitle("Advanced Arithmetics")

integer1 = -32
float1 = -17.13579

print("***** Absolute Value: abs(x)")
print("abs(", integer1, ") = ", abs(integer1), sep='')
print("abs(", float1, ") = ", abs(float1), sep='')

print("\n***** Round: round(x)")
print("round(", float1, ") = ", round(float1), sep='')
print("round(", float1, ", 2) = ", round(float1, 2), sep='')
print("round(", float1, ", 4) = ", round(float1, 4), sep='')

print("\n***** Power: pow(x, y)")
print("pow(2, 10) =", pow(2, 10))
print("pow(2.0, 10) =", pow(2.0, 10))

print("\n***** Minimum and Maximum: min() max()")
print("min(1, 3, 5, 7, 9) =", min(1, 3, 5, 7, 9))
print("max(1, 3, 5, 7, 9) =", max(1, 3, 5, 7, 9))

print("\n***** math.fabs() and math.pow()")
print("math.fabs() is an equivalent to standard abs(), and ")
print("math.pow() is an equivalent to standard pow(), except ")
print("they will always return a float value")
print("math.fabs(", integer1, ") = ", math.fabs(integer1), sep='')
print("math.pow(2, 10) =", math.pow(2, 10))

