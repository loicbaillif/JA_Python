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
ANIMALS_PRICES = (CHICKEN_PRICE, GOAT_PRICE, PIG_PRICE, COW_PRICE, SHEEP_PRICE)
MONEY_TEST = (1, 22, 23, 444, 678, 900, 1296, 3000, 3848, 5000, 6769, 7000, 90000)


# Functions
def most_useful(money):
    # for the given money, returns the most expansive animal that can be bought
    rank = 0
    for animal in ANIMALS_PRICES:
        if money >= animal:
            rank += 1
    return rank  


def how_many_to_buy(money, animal_price):
    return int(money/animal_price)


def provide_singular_plural(quantity, animal_rank):
    if quantity > 1:
        return ANIMALS_NAMES_PLURAL[animal_rank]
    return ANIMALS_NAMES_SINGULAR[animal_rank]


# Tests
for test in MONEY_TEST:
    animal_to_buy_t = most_useful(test)
    qty_to_buy_t = how_many_to_buy(test, ANIMALS_PRICES[animal_to_buy_t - 1])
    print(f'{qty_to_buy_t} {provide_singular_plural(qty_to_buy_t, animal_to_buy_t)}' if qty_to_buy_t > 0 else 'None')


# Answer
player_money = int(input())
animal_to_buy = most_useful(player_money)  # Index position
qty_to_buy = how_many_to_buy(player_money, ANIMALS_PRICES[animal_to_buy - 1])
print(f'{qty_to_buy} {provide_singular_plural(qty_to_buy, animal_to_buy)}' if qty_to_buy > 0 else 'None')


print_title("End of exercise")