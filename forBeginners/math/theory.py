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

print("\n***** math.log()")
print("math.log(x, y) will return the number z so that math.pow(y, z) = x")
print("math.log(x) will return math.log(x, e) (the math constant)")
print("math.log(128, 2) =", math.log(128, 2))
print("math.log(128) =", math.log(128))

print("\n***** Floor and Ceiling: math.floor(), math.ceil()")
print("math.floor(a) returns the highest integer lower or equal to a")
print("math.floor(", float1, ") = ", math.floor(float1), sep='')
print("math.ceil(a) returns the lowest integer higher or equal to a")
print("math.ceil(", float1, ") = ", math.ceil(float1), sep='')

print("\n***** Square root: math.sqrt()")
print("math.sqrt(x) returns the square root for x")
print("This is equivalent to math.pow(x, 0.5)")
print("math.sqrt(16) =", math.sqrt(16))
print("math.pow(16, 0.5) =", math.pow(16, 0.5))