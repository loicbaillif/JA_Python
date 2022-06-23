#  ******** JetBrains Academy - Python for Beginners ********
#  ****** While loop ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Exercise - Factorial ".center(80, "*"))
print(separator.center(80)+"\n")

# Factorial of the number N is the result of the multiplication of all 
# positive integers less than or equal to N. For example, the factorial of 3 
# is the product of 3, 2, 1, i.e. 3! = 3 x 2 x 1 = 6. Now, your task is to try 
# and write a program that calculates the factorial of the input number 
# using while loop.
#
#  The input format:
#   The number N in range from 1 to 100.
#
# The output format:
#   The factorial N!.

n_input = int(input("Please enter a number between 0 and 100:\n> "))
factorial_n = 1
while n_input > 1:
    factorial_n *= n_input
    n_input -= 1
print(factorial_n)