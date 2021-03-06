#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Comparisons ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Comparisons: Exercise - Very Odd ".center(80, "*"))
print(separator.center(80)+"\n")

# Find out if the result of dividing A by B is an odd number.
#
# The input format:
#   The first line is the dividend (A) and the second line is the divisor (B).
#   It is guaranteed that the numbers are divided without remainder.
#
# The output format:
#   True or False

print(int(input()) / int(input()) % 2 == 1)