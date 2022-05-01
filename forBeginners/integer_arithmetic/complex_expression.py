# ****** Python for Beginners - Integer arithmetic ******
# ****** Exercise : Integer Arithmetic ******
#
# Write a program that takes a single integer number n and then performs 
# the following operations in the following order:
#   1. adds n to itself
#   2. multiplies the result by n
#   3. subtracts n from the result
#   4. exactly divides the result by n (that means, you need to carry out 
#   integer division).
# 
# Then print the result of the division. 

n = int(input())

print(((n + n) * n - n) // n)