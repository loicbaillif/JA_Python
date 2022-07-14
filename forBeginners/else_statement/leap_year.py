#  ******** JetBrains Academy - Python for Beginners ********
#  ****** else statement ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" else statement: Exercise - Healthy Sleep ".center(80, "*"))
print("_"*40+"\n\n")

# Write a program that checks if a year is leap.
#
# A year is considered leap if it is divisible by 4 and NOT divisible by 100, 
# or if it is divisible by 400. So, 2000 is leap and 2100 isn't.
#
# Output either "Leap" or "Ordinary" depending on the input.

def divisible(x, y):
    # returns true if x is divisible by y, false elsewhere
    return x % y == 0

year = int(input())
if (divisible(year, 4) and not divisible(year, 100)) or divisible(year, 400):
    print("Leap")
else:
    print("Ordinary")