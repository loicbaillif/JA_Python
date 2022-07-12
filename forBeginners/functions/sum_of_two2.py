#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Invoking a function ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Invoking a function - Exercise: Sum of two ".center(80, "*"))
print(("_"*40).center(80, " ") + "\n\n")

def get_sum(a, b):
    return a + b

x = int(input("Enter the first number:\n> "))
y = int(input("Enter the second number:\n> "))
print(f"{x} + {y} = {get_sum(x, y)}")