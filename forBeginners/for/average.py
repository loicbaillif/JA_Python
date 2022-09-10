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


a = int(input())
b = int(input())

while a % 3 != 0:
    a += 1

while b % 3 != 0:
    b -= 1

print((a + b) / 2)

print_title("End of exercise")