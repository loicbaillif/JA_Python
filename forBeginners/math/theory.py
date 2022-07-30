#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Theory ******

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
