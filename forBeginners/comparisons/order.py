#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Comparisons ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Comparisons: Exercise - Order! ".center(80, "*"))
print(separator.center(80)+"\n")

# Get three large numbers from input and check that they are given in 
# ascending order. The subsequent number must be greater than the 
# previous one.

input1 = int(input())
input2 = int(input())
input3 = int(input())

print(input2 > input1 and input3 > input2)  # Tested => OK