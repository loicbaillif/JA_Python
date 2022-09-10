#  ******** JetBrains Academy - Python for Beginners ********
#  ****** for loop: Exercise - Average of all numbers ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("for loop: Exercise - Average of all numbers")


# https://hyperskill.org/learn/step/6071
# Write a program that reads 2 numbers, a and b, from the input. As an output, 
# it shows the mean of all numbers that lie on the interval between 
# a and b (included), and are divisible by 3.

sum_elements = 0
nb_elements = 0

a = int(input())
b = int(input())

for i in range(a, b + 1):
    if (i % 3 == 0):
        sum_elements += i
        nb_elements += 1

print(sum_elements / nb_elements)

print_title("End of exercise")