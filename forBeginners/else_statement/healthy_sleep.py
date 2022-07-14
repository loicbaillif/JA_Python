#  ******** JetBrains Academy - Python for Beginners ********
#  ****** else statement ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" else statement: Exercise - Healthy Sleep ".center(80, "*"))
print("_"*40+"\n\n")

a = int(input("Please enter the minimum number of sleep hours per day:\n> "))
b = int(input("Please enter the maximum number of sleep hours per day:\n> "))
h = int(input("Please enter the number of hours you sleep per day:\n> "))

if h < a:
    print("Deficiency")
elif h > b:
    print("Excess")
else:
    print("Normal")