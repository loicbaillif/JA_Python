#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Scope: Exercise - Hero Damage ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Scope: Exercise - Hero Damage ".center(80, "*"))
print("_"*40+"\n\n")

# Let's now take a look at how global variables can help us to save 
# information between different function calls.
# Imagine you're writing a program for some video game: you need to calculate 
# the damage that the main hero deals to the enemies in one hit. The current 
# damage is stored in the global variable hero_damage. Use the power of this 
# global and write three functions that change its value:
#   . double_damage() doubles the damage of the hero
#   . disarmed() makes the damage equal to 10% of the current value
#   . power_potion() adds 100 damage points

hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage = hero_damage * 2


def disarmed():
    global hero_damage
    hero_damage = hero_damage / 10


def power_potion():
    global hero_damage
    hero_damage = hero_damage + 100