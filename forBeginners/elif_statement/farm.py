#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - The farm ******

# 

# Local application imports
from asyncio.windows_events import NULL
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

# Variables
CHICKEN_PRICE = 23
GOAT_PRICE = 678
PIG_PRICE = 1296
COW_PRICE = 3848
SHEEP_PRICE = 6769
ANIMALS_NAMES_SINGULAR = ('None', 'chicken', 'goat', 'pig', 'cow', 'sheep')
ANIMALS_NAMES_PLURAL = ('None', 'chickens', 'goats', 'pigs', 'cows', 'sheep')
ANIMALS_PRICES = (SHEEP_PRICE, COW_PRICE, PIG_PRICE, GOAT_PRICE, CHICKEN_PRICE)
MONEY_TEST = (1, 22, 23, 444, 678, 900, 1296, 3000, 3848, 5000, 6769, 7000, 90000)

player_money = int(input())

if player_money >= SHEEP_PRICE:
    print(f'{int(player_money / SHEEP_PRICE)} sheep')
elif player_money >= COW_PRICE:
    print('1 cow')  # 2 cows are more expansive than one sheep ...
elif player_money >= PIG_PRICE:
    nb_pigs = int(player_money / PIG_PRICE)
    print(f'{nb_pigs} pig', 's' if nb_pigs > 1 else '', sep='')
elif player_money >= GOAT_PRICE:
    print('1 goat')
elif player_money >= CHICKEN_PRICE:
    nb_chickens = int(player_money / CHICKEN_PRICE)
    print(f'{nb_chickens} chicken', 's' if nb_chickens > 1 else '', sep='')
else:
    print('None')



print_title("End of exercise")