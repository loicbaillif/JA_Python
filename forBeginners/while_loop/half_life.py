#  ******** JetBrains Academy - Python for Beginners ********
#  ****** While Loop ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Exercise - Half-life ".center(80, "*"))
print(separator.center(80)+"\n")

initial_quantity = int(input("Please enter initial quantity of Radium:\n"))
final_quantity = int(input("Please enter final quantity to reach:\n"))
nb_half_life = 0
days_per_half_life = 12  # avoid magic numbers ...

while initial_quantity > final_quantity:
    nb_half_life += 1
    initial_quantity /= 2

nb_days = nb_half_life * days_per_half_life  # Thank you Marie Curie :)
print("You will reach that quantity in " + str(nb_days) + " days.")
