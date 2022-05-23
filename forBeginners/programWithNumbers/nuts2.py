# ****** Python for Beginners - Program with numbers ******
# ****** Exercise : Divide nuts equally between squirrels ******
#
# N squirrels found K nuts and decided to divide them equally. 
# Determine how many nuts each squirrel will get and print the result.
#
# Input data format 
# There are two positive integers N and K, neither of them 
# is greater than 10000.

squirrels = int(input())
nuts = int(input())

print(nuts // squirrels)