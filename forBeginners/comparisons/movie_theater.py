#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Comparisons: Exercise******
# The movie theater has cinema halls that can accommodate a certain number 
# of viewers each day. Figure out if a movie theater can hold a given number 
# of viewers that plan to visit it on a particular day.
#
# The input format
#   The first line is number of halls, the second line is their capacity, 
#   and the third line is the planned number of viewers.
#
# The output format
#   True or False.


separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Comparisons: Exercise - Movie theater".center(80, "*"))
print(separator.center(80)+"\n\n")

number_of_halls = int(input())
capacity_per_hall = int(input())
planned_visitors = int(input())
print(planned_visitors <= number_of_halls * capacity_per_hall)