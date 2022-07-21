#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - The army of units ******

# In a computer game, each gamer has an army of units.
# Write a program that will classify the army of your enemies corresponding 
# to the following rules:
#   Units: Category
#       . less than 1: no army
#       . from 1 to 9: few
#       . from 10 to 49: pack
#       . from 50 to 499: horde
#       . from 500 to 999: swarm
#       . 1000 and more: legion
# The program should read the number of units and output the corresponding category.

# Local application imports
from print_title import print_title
from print_title import print_subtitle

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - The army of units")

# number_units = int(input())
def unit_size(number_units):
    if number_units < 1:
        print(f"{number_units} --> no army")
    elif number_units < 10:
        print(f"{number_units} --> few")
    elif number_units < 50:
        print(f"{number_units} --> pack")
    elif number_units < 500:
        print(f"{number_units} --> horde")
    elif number_units < 1000:
        print(f"{number_units} --> swarm")
    else:
        print(f"{number_units} --> legion")



test_list = (0, 1, 9, 10, 11, 49, 50, 51, 499, 500, 501, 999, 1000, 2000)
for elt in test_list:
    unit_size(elt)