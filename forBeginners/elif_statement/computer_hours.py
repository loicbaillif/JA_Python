#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - Computer Hours ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - Computer Hours")


# Write a program that asks a user how long, on average, they spend on 
# a computer per day. If it's less than 2 hours, the program should output 
# "That's rare nowadays!". If it is 2 hours or more, but less than 4 hours 
# per day it should output"This seems reasonable". In any other case, 
# output "Don't forget to take breaks!"

nb_hours = int(input("How long (average) do you spend on a computer per day?\n> "))

if nb_hours < 2:
    print("That's rare nowadays!")
elif nb_hours < 4:
    print("This seems reasonable")
else:
    print("Don't forget to take breaks!")


print_title("End of exercise")