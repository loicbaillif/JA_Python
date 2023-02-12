#  ******** JetBrains Academy - Python for Beginners ********
#  ****** for loop: Exercise - A mean of n ******
# https://hyperskill.org/learn/daily/6818

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("for loop: Exercise - A mean of n")

# Variables
nb_elements = int(input())
sum = 0

for _ in range(nb_elements):
    sum += int(input())

print(sum/nb_elements)


print_title("End of exercise")
