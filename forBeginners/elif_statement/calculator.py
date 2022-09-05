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
first_number = float(input("Please enter the first number:\n> "))
second_number = float(input("Please enter the second number:\n> "))
operation = input("Please enter the operation:\n> ")
forbidden_division = "Division by 0!"
result = f"Result:\n\t{first_number} {operation} {second_number} = "

if operation.isalpha():
    if operation == "mod":
        result += str(forbidden_division if (second_number == 0) else (first_number % second_number))
    elif operation == "pow":
        result += str(first_number ** second_number)
    else:
        # We don't consider input errors yet, so this must be "div"
        result += str(forbidden_division if (second_number == 0) else (first_number // second_number))
else:
    print("+, -, * or / requested")
    if operation == "+":
        result += str(first_number + second_number)
    elif operation == "-":
        result += str(first_number - second_number)
    elif operation == "*":
        result += str(first_number * second_number)
    else:
        result += str(forbidden_division if (second_number == 0) else (first_number / second_number)) 

print(result)

print_title("End of exercise")