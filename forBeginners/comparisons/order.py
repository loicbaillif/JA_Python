#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Comparisons ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Comparisons: Exercise - Order! ".center(80, "*"))
print(separator.center(80)+"\n")

# Get three large numbers from input and check that they are given in 
# ascending order. The subsequent number must be greater than the 
# previous one.

input1 = input("Please enter first number:\n")
input2 = input("Please enter second number:\n")
input3 = input("Please enter third number:\n")

print(input1 < input2 < input3)  # Tested => OK