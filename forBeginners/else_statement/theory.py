#  ******** JetBrains Academy - Python for Beginners ********
#  ****** else statement ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" else statement: Theory ".center(80, "*"))
print("_"*40+"\n\n")

# First example:
today = "working day"
holiday = "holiday"
if today == holiday:
    print("Lucky you!")
else:
    print("Keep your chin up, then.")

# Second example, ternary operator:
hour = 13
sunrise = 7
sunset = 19
print("Day time!" if (hour >= sunrise and hour <= sunset) else "Night time!")

print("_"*40+"\n\n")