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

# Nested if else:
x_input = int(input("Please enter an integer"))
if x_input < 100:
    print("Less than a hundred")
else: 
    if x_input == 100:
        print("Right on it!")
    else:
        print("More than a hundred")
    print("We are still in the main 'else'")

# Conclusion:
print("Keyword 'else' provides an alternative")
print("It will be executed in case 'if' statement is not")
print("It does not require any condition")
print("if / else statement can be nested")

print("_"*40+"\n\n")