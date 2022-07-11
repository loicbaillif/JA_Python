#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Declaring a function ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Declaring a function - Exercise: Make it work ".center(80, "*"))
print(("_"*40).center(80, " ") + "\n\n")


def closest_higher_mod_5(x):
    remainder = x % 5
    return x + 5 * (remainder != 0) - remainder

print(closest_higher_mod_5(40))
print(closest_higher_mod_5(43))