#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Load Module: Exercise - Not exactly random ******


# Python can generate random numbers using the random module. To do that, 
# it takes one number as a starting point (it's called seed) and then uses 
# a formula. By default, the current system time is used as seed. 
# However, we can set the seed manually and thus make sure that our "random" 
# number is always the same regardless of how many times we run the program.
#
# Write a program that takes an integer number n, sets the seed to that 
# number, and then prints a random number from -100 to 100.
# 
# Use the seed and randint functions from the random module. The former takes 
# one number and the latter takes two numbers that represent the range.

 # Standard library imports
from random import randint
from random import seed

# Local application imports
from print_title import print_title
from print_title import print_subtitle

print_title("Jet Brains Academy - Python for Beginners")
print_subtitle("Load Module: Exercise - Not exactly random")

n = int(input("Please enter the int number to be used as seed:\n> "))
bound = 100
seed(n)
print(randint(-bound, bound))