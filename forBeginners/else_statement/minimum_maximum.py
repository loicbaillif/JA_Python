#  ******** JetBrains Academy - Python for Beginners ********
#  ****** else statement ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" else statement: Exercise - Minimum Maximum ".center(80, "*"))
print("_"*40+"\n\n")

input_1 = int(input())
input_2 = int(input())

if input_1 <= input_2:
    print(f"{input_2} \n{input_1}")
else:
    print(f"{input_1} \n{input_2}")