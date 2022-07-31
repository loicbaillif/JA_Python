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
print("\tabs(", integer1, ") = ", abs(integer1), sep='')
print("\tabs(", float1, ") = ", abs(float1), sep='')

print("\n***** Round: round(x)")
print("\nround(", float1, ") = ", round(float1), sep='')
print("\tround(", float1, ", 2) = ", round(float1, 2), sep='')
print("\tround(", float1, ", 4) = ", round(float1, 4), sep='')

print("\n***** Power: pow(x, y)")
print("\tpow(2, 10) =", pow(2, 10))
print("\tpow(2.0, 10) =", pow(2.0, 10))

print("\n***** Minimum and Maximum: min() max()")
print("\tmin(1, 3, 5, 7, 9) =", min(1, 3, 5, 7, 9))
print("\tmax(1, 3, 5, 7, 9) =", max(1, 3, 5, 7, 9))

print("\n***** math.fabs() and math.pow()")
print("math.fabs() is an equivalent to standard abs(), and ")
print("math.pow() is an equivalent to standard pow(), except ")
print("they will always return a float value")
print("\tmath.fabs(", integer1, ") = ", math.fabs(integer1), sep='')
print("\tmath.pow(2, 10) =", math.pow(2, 10))

print("\n***** math.log()")
print("math.log(x, y) will return the number z so that math.pow(y, z) = x")
print("math.log(x) will return math.log(x, e) (the math constant)")
print("\tmath.log(128, 2) =", math.log(128, 2))
print("\tmath.log(128) =", math.log(128))

print("\n***** Floor and Ceiling: math.floor(), math.ceil()")
print("math.floor(a) returns the highest integer lower or equal to a")
print("\tmath.floor(", float1, ") = ", math.floor(float1), sep='')
print("math.ceil(a) returns the lowest integer higher or equal to a")
print("\tmath.ceil(", float1, ") = ", math.ceil(float1), sep='')

print("\n***** Square root: math.sqrt()")
print("math.sqrt(x) returns the square root for x")
print("This is equivalent to math.pow(x, 0.5)")
print("\tmath.sqrt(16) =", math.sqrt(16))
print("\tmath.pow(16, 0.5) =", math.pow(16, 0.5))
print("\n")


print_subtitle("Geometry")
print("***** Pi")
print("we have access to the number Pi via math.pi")
pizza_diameter = 26
print("A pizza has a diameter of 26cm")
print("Its circumference measures ", 
        round(math.pi * pizza_diameter, 1), "cm", sep='')
print("Its surface measures ", 
        round(math.pi * math.pow((pizza_diameter / 2), 2), 2), "cm²", sep='')

print("\n***** Trigonometry")
print("math.cos(A) returns the cosine of A radians")
print("math.sin(A) returns the sine of A radians")
print("math.degrees(A) returns angle A converted from radians to degrees")
print("math.radians(A) returns angle A converted from degrees to radians")
aDeg = 60
aRad = math.radians(aDeg)
aCos = math.cos(aRad)
aSin = math.sin(aRad)
print("\tmath.radians(60) =", aRad)
print("\tmath.cos(math.radians(60)) =", round(aCos, 2), "(1/2) ==> aCos")
print("\tmath.sin(math.radians(60)) =", round(aSin, 2), "(sqrt(3)/2) ==> aSin")
print("aCos² + aSin² = ...", 
    math.pow(math.cos(math.radians(60)), 2) 
    + math.pow(math.sin(math.radians(60)), 2))
print("CQFD.")
