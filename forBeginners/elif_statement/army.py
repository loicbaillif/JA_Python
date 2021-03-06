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

pack = 50
horde = 500

number_units = int(input("Please enter the number of units"))
if number_units < pack:
    if number_units < 1:
        print("no army")
    elif number_units < 10:
        print("few")
    else:
        print("pack")
else:
    if number_units < horde:
        print("horde")
    elif number_units < 1000:
        print("swarm")
    else: 
        print("legion")
