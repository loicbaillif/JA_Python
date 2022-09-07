#  ******** JetBrains Academy - Python for Beginners ********
#  ****** for loop: Exercise - Lucky 7 ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("for loop: Exercise - Lucky 7")


# https://hyperskill.org/learn/step/6549
# Read the first input – a number n. Then read input n times. 
# Each time you'll get an integer value. If it's a multiple of 
# 7 (can be divided by 7 without a remainder), print its square on a new line. 
# Note that you don't need to perform any calculations 
# on the first input (the n).

nb_elements = int(input("How many elements will be treated?\n> "))
result_list = []
for element in range(nb_elements):
    user_input = int(input(f"Please enter element n°{element + 1}:\n> "))
    if user_input % 7 == 0:
        result_list.append(user_input ** 2)

for elt in result_list:
    print(elt)


print_title("End of exercise")