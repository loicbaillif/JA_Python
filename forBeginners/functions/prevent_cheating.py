#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Declaring a function ******

import math


print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Declaring a function: Exercise - Prevent Cheating ".center(80, "*"))
print(" " * 20 + "_" * 40 + " " * 20 +"\n\n")

print(math.factorial(4))

def new_math_factorial(number):
    print("Don't cheat!")

math.factorial = new_math_factorial

print(math.factorial(4))

print(" " * 20 + "_" * 40 + " " * 20 +"\n\n")