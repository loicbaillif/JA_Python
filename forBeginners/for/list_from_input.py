#  ******** JetBrains Academy - Python for Beginners ********
#  ****** for loop: Exercise - List from input ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("for loop: Exercise - List from input")

# https://hyperskill.org/learn/step/6739
# Use the template below to write a program that takes n numbers as input, 
# creates a list from them, and then prints it.
#
# The first number in the sample input shows how many elements your list 
# should contain. The numbers after it are the elements that you need 
# to append to your list.

list_elements = []
for _ in range(int(input())):
    list_elements.append(int(input()))

print(list_elements)

print_title("End of exercise")