#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Declaring a function ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Declaring a function - Exercise: Miles away ".center(80, "*"))
print(("_"*40).center(80, " ") + "\n\n")

km_per_mile = 1.609  # Create conversion variable to avoid magic number

def miles_away(distance):
    return distance * km_per_mile

distance_miles = int(input("Please enter the distance in miles:\n> "))
print(f"{distance_miles} miles = {miles_away(distance_miles)} km.")