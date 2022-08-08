#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - The farm ******

# 

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - The farm")

# In a farming game, you can buy certain animals for a specific price. 
# As a player, you want to buy the most useful (i.e. the most expensive) 
# animal. Here are the animals and their prices:
#   Item:       Price
#   Chicken:    23
#   Goat:       678
#   Pig:        1296
#   Cow:        3848
#   Sheep:      6769

# Write a program that determines what is the most expensive animal that the 
# user can buy with their money and how many of them they can buy.
# Note that you should only find one kind of animal to buy (the most expensive 
# one). You don't need to mention any alternative options. For example, if the 
# user has 710 coins, your program should output # 1 goat, but not 
# 1 goat\n30 chickens or anything like that.

# The input format:
#   The money that the user has.
# The output format:
#   How many animals the user can afford, for example, 20 chickens. 
#   If the user cannot afford any animal, write None.