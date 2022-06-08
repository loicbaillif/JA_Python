#  ******** JetBrains Academy - Python for Beginners ********
#  ****** While Loop ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Exercise - Half-life ".center(80, "*"))
print(separator.center(80)+"\n")

initial_quantity = int(input())
final_quantity = int(input())
nb_half_life = 0
days_per_half_life = 12

while initial_quantity > final_quantity:
    nb_half_life += 1
    initial_quantity /= 2

nb_days = nb_half_life * days_per_half_life
print(nb_days)
