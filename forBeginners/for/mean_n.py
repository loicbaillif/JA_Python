#  ******** JetBrains Academy - Python for Beginners ********
#  ****** for loop: Exercise - A mean of n ******
# https://hyperskill.org/learn/daily/6818

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("for loop: Exercise - A mean of n")

# Variables
nb_elements = int(input())
elements_sum = 0

for _ in range(int(input())):
    elements_sum += int(input())

print(elements_sum / nb_elements)


print_title("End of exercise")
