#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Invoking a function ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Invoking a function - Exercise: Sum of two numbers ".center(80, "*"))
print(("_"*40).center(80, " ") + "\n\n")

print("This program will print the sum of two numbers, given by user.")
x = int(input("Please enter the first number:\n> "))
y = int(input("Please enter the second number:\n> "))
print(f"{x} + {y} = {sum((x, y))}")