#  ******** JetBrains Academy - Python for Beginners ********
#  ****** While Loop ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Exercise - 55 is enough".center(80, "*"))
print(separator.center(80)+"\n")

nb_inputs = 0
sum_inputs = 0
final_number = 55  # Avoid magic numbers
user_input = int(input())  # Needed for first input

while user_input != final_number:
    nb_inputs += 1
    sum_inputs += user_input    
    user_input = int(input())  # Important to put this as last line

print(nb_inputs)
print(sum_inputs)
print(round(sum_inputs / nb_inputs))