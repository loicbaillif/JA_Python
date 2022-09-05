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

# VARIABLES
first_number = float(input())
second_number = float(input())
operation = input()
forbidden_division = "Division by 0!"

if operation.isalpha():
    if operation == "mod":
        print(forbidden_division if (second_number == 0.0) else (first_number % second_number))
    elif operation == "pow":
        print(first_number ** second_number)
    else:
        # We don't consider input errors yet, so this must be "div"
        print(forbidden_division if (second_number == 0.0) else (first_number // second_number))
else:
    print("+, -, * or / requested")

print_title("End of exercise")