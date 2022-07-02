#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Declaring a function ******

import math


print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Declaring a function: Exercise - Prevent Cheating ".center(80, "*"))
print(" " * 20 + "_" * 40 + " " * 20 +"\n\n")


def new_math_factorial(number):
    print("Don't cheat!")

math.factorial = new_math_factorial



print(" " * 20 + "_" * 40 + " " * 20 +"\n\n")