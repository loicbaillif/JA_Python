#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - Calculator ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - Calculator")

# Let's write a simple calculator!
# 
# It will read 3 lines:
#   - the first number
#   - the second number
#   - the arithmetic operation.
# Numbers are floats!
#
# The output is the result of the following: first_number operation second_number.
#
# Operations are: +, -, /, *, mod, pow, div.

first_number = float(input())
second_number = float(input())
operation = input()

if operation.isalpha():
    print("mod, pow or div requested")
else:
    print("+, -, * or / requested")

print_title("End of exercise")