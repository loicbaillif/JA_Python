#  ******** JetBrains Academy - Python for Beginners ********
#  ****** for loop: Exercise - FizzBuzz ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("for loop: Exercise - FizzBuzz")


# https://hyperskill.org/learn/step/8442
# FizzBuzz is a famous code challenge used in interviews to test basic 
# programming skills. It's time to write your own implementation.
#
# Print numbers from 1 to 100 inclusively following these instructions:
#   - if a number is multiple of 3, print "Fizz" instead of this number
#   - if a number is multiple of 5, print "Buzz" instead of this number
#   - for numbers that are multiples of both 3 and 5, print "FizzBuzz"
#   - print the rest of the numbers unchanged.
#
# Output each value on a separate line.

for number in range(101):
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print(number)

print_title("End of exercise")