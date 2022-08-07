#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - Calculating the factorial ******

# Global Python import
from math import factorial

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions - Exercise: Calculating the factorial")

# Import the factorial function from the math module  
# and print the value of the factorial of x.

user_input = int(input())
print(factorial(user_input))



print_title("End of exercise")