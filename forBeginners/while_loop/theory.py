#  ******** JetBrains Academy - Python for Beginners ********
#  ****** WHILE loop ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Theory ".center(80, "*"))
print("_"*40+"\n\n")
print(" 1) Simple while loop ".center(60, "#"))
number = 0
while number < 5:
    print(number)
    number += 1
print("Loop is complete, number = " + str(number))

print("_"*30+"\n")
print(" 2) Infinite while loop ".center(60, "#"))
# Besides having it as a bug, it may be relevant in some cases (?)
# while True:
#     print("Neverending story")

