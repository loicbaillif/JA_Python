#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif: Exercise - Coordinates ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif: Exercise - Coordinates")



# Locate a point on the Cartesian coordinate plane: 
# which of four quadrants does a point belong to?
#
# Read two numbers from the input, not necessarily integers, the first number 
# will indicate a position on the X-axis, the second one — on the Y-axis. 
# Let's keep referring to the quadrants by Roman numerals, as detailed:
#       I   = X > 0, Y > 0
#       II  = X < 0, Y > 0
#       III = X < 0, Y < 0
#       IV  = X > 0, Y < 0
#
# If a point is the origin (0, 0), print "It's the origin!". In case of a 
# point lying on the axes, with either x = 0 or y = 0, 
# print "One of the coordinates is equal to zero!".

x_coordinate = float(input())
y_coordinate = float(input())

if x_coordinate * y_coordinate == 0:
    if x_coordinate == y_coordinate:
        print("It's the origin!")
    else:
        print("One of the coordinates is equal to zero!")
elif x_coordinate > 0:
    if y_coordinate > 0:
        print("I")
    else: 
        print("IV")
else:
    if y_coordinate > 0:
        print("II")
    else:
        print("III")



print_title("End of exercise")