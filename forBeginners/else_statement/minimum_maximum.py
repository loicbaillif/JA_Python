#  ******** JetBrains Academy - Python for Beginners ********
#  ****** else statement ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" else statement: Exercise - Minimum Maximum ".center(80, "*"))
print("_"*40+"\n\n")

input1 = int(input())
input2 = int(input())

if input1 <= input2:
    print(f"{input1} \n{input2}")
else:
    print(f"{input2} \n{input1}")