#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Invoking a function ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Invoking a function: Theory ".center(80, "*"))
print("_"*40+"\n\n")
print(" 1) Invoking print() ".center(60, "*"))
print("Hello, World!")      # Invoking print() with 1 argument
print()                     # Invoking print() with no argument
print("Bye,", "then!")      # Invoking print() with 2 arguments
print("Lorem", "Ipsum", "Dolor", "Sit", "Amet", sep=".", end="\n\t")
print("test\n")

print(" 2) Built-in functions ".center(60, "*"))
number = "1234"
print(f"number = \"1234\"\nlen(number) = {len(number)}")
integer = int(number)           # 1234
float_number = float(number)    # 1234.0
print(f"int(number) = {integer} - float(number) = {float_number}")
my_sum = sum((integer, float_number))
print(f"sum((integer, float_number)) = {my_sum}")
print(f"round(my_sum) = {round(my_sum)}")
integer = 3
float_number = 5.4
my_sum = integer + float_number
print(min(integer, float_number))
print(type(max(integer, float_number, my_sum)))
