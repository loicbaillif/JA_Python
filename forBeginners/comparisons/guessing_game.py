#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Comparisons ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Comparisons: Exercise - Guessing game".center(80, "*"))
print(separator.center(80)+"\n\n")

set_number = 6557

user_input1 = int(input())
user_input2 = int(input())
print(set_number == user_input1 * user_input2)