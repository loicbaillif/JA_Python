#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - Through the doorway ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - Through the doorway")


# Suppose you want to carry a box with dimensions 
# A × B × C (length × width × height) through the doorway with dimensions 
# X × Y (width × height). Write a program to check whether it is possible.

# The input format:
# The input comprises five strings with numbers in the following order: 
#   A, B, C, X, Y. 
# If the size of the doorway is greater than or equal to any two dimensions 
# of the box, it is considered that the box can be carried.

# The output format:
# If the box can be carried through the doorway, output 
# "The box can be carried".
# If it cannot be carried, output "The box cannot be carried".


box = [int(input()), int(input()), int(input())]
box.sort()
door = [int(input()), int(input())]
door.sort()

if box[0] <= door[0]:
    if box[1] <= door[1]:
        print("The box can be carried")
else:
    print("The box cannot be carried")



print_title("End of exercise")