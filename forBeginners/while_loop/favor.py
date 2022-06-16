#  ******** JetBrains Academy - Python for Beginners ********
#  ****** While Loop ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Exercise - Favor ".center(80, "*"))
print(separator.center(80)+"\n")

# Carl asks you to count the sum of the first k natural numbers. 
# Read k from the input, then add up numbers from 1 to k and print your answer.

k_input = int(input())
sum = 0
while k_input > 0:
    sum += k_input
    k_input -= 1
print(sum)