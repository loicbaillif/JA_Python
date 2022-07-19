#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Load Module: Theory ******

# Standard library imports
import math 
from random import choice
from string import digits

# Local application imports
from print_title import print_title
from print_title import print_subtitle

print_title("JetBrains Academy - Python for Beginners")
print_title("Load Module")

print_subtitle("Module Loading")
print("Recommended import order:")
print("\t1. Standard library imports")
print("\t2. Third party dependency import")
print("\t3. Local application imports")
print("Group them by category, and leave an empty line between 2 categories")

print_subtitle("Built-in Modules")
print("math.factorial(6) = " + str(math.factorial(6)))  # 720
print("math.log(10) = " + str(math.log(10)))
print("math.pi = " + str(math.pi))
print("math.e = " + str(math.e))
print(digits)
# Here-after: print a random item from the list
print(choice(["red", "yellow", "blue", "green"]))  
