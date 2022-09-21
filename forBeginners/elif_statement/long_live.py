#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - Long live the king ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - Long live the king")

# https://hyperskill.org/learn/step/8441
# Let's imagine a chessboard, the squares on which are marked with coordinates. 
# The coordinates are numbers between 1 and 8 inclusively. The first number 
# indicates a column, the second one indicates a row.
#
# The chess king can stand on any square and can move one step horizontally, 
# vertically, or diagonally in any direction within the board.
#
# The input will contain the coordinates on which the king is located. 
# You should figure out and print how many moves the figure can make: 
# for example, from the position (1, 8), the king can make 
# only 3 moves (right, down, diagonally).


x_king = int(input())
y_king = int(input())

if (1 < x_king < 8) and (1 < y_king < 8):
    print(8)
elif (x_king in (1, 8)) and (1 < y_king < 8):
    print(5)
elif (1 < x_king < 8) and (y_king in (1, 8)):
    print(5)
else:
    print(3)


print_title("End of exercise")