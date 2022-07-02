#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Declaring a function ******

from audioop import mul


print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Declaring a function: Theory ".center(80, "*"))
print("_"*40+"\n\n")

print(" First example ".center(60, "*"))
def multiply(x, y):
    return x * y

print(multiply(3, 4))
print(multiply(6, 3))

def praise():
    return "Of course you are the best!"

print(praise())
print(praise().center(50, "~"))
