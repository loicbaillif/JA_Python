#  ******** JetBrains Academy - Python for Beginners ********
#  ****** While Loop ******

# Write a program that prints all positive even numbers less than the input 
# number. Please, use the while loop for that.
#
# The input format:
#   The maximum number N varying from 1 to 200.
#
# The output format:
#   All positive even numbers that are less than N. Print them in  
#   the ascending order. Each number must be on a separate line.

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Exercise - Find even".center(80, "*"))
print(separator.center(80)+"\n")

max_number = int(input())
output = 2
while (output < max_number):
    print(output)
    output += 2