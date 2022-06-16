#  ******** JetBrains Academy - Python for Beginners ********
#  ****** While Loop ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Exercise - Favor ".center(80, "*"))
print(separator.center(80)+"\n")

# Carl asks you to count the sum of the first k natural numbers. 
# Read k from the input, then add up numbers from 1 to k and print your answer.

k_input = int(input("Please enter an integer number:\n> "))
sum_first_k = 0
i = 0
while i <= k_input:
    sum_first_k += i
    i += 1
print(f"The sum of the first {k_input} numbers is {sum_first_k}.")