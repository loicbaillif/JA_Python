# ****** Python for Beginners - Program with numbers ******
# ****** Exercise : How many nuts will be left after division ******
#
# N squirrels found K nuts and decided to divide them equally. 
# Find how many nuts will be left after each of the squirrels takes an 
# equal number of nuts.
#
# Input data format 
# There are two positive integers N and K, neither of them 
# is greater than 10000.

squirrels = int(input())
nuts = int(input())

print(nuts % squirrels)