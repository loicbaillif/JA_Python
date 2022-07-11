#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Declaring a function ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Declaring a function - Exercise: Make it work ".center(80, "*"))
print(("_"*40).center(80, " ") + "\n\n")


def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    return "I don't know :("