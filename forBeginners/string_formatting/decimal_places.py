#  ******** JetBrains Academy - Python for Beginners ********
#  ****** String Formatting: Exercise - Decimal Places ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("String Formatting: Exercise - Decimal Places")


# Round the number from input to the required number of decimals.

# The input format:
# Two lines: 
#   the first with a floating-point number, 
#   the second with an integer representing the decimal count.
#
# The output format:
#   A formatted string containing the rounded number.

user_input_float = float(input())
user_input_precision = int(input())

print(f"{user_input_float:.{user_input_precision}f}")


print_title("End of exercise")