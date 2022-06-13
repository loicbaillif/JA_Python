#  ******** JetBrains Academy - Python for Beginners ********
#  ****** While Loop ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Exercise - Square up ".center(80, "*"))
print(separator.center(80)+"\n")

# The program below is supposed to print the squares of all numbers 
# from 1 to 20 (including), but there are some mistakes. Find and fix them.

i = 1
upper_limit = 20  # Create a variable to avoid magic number. #GoodPractice :D
while i <= upper_limit:   # Correct the comparison sign : <= instead of >
    print(i * i)  # Program supposed to print  the squares : i * i instead of i
    i += 1        # Crucial: increment loop variable, or infinite loop