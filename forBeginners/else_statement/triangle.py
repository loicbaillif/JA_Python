#  ******** JetBrains Academy - Python for Beginners ********
#  ****** else statement ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" else statement: Exercise - Triangle or not ".center(80, "*"))
print("_"*40+"\n\n")

# Read three angles given on separate input lines and check whether 
# they form a triangle. Print the answer in the following format: 
#   "The triangle is valid!" or "The triangle is not valid!".

a = int(input())
b = int(input())
c = int(input())
sum_angles = 180  # Avoid using magic numbers
valid = "" if a + b + c == sum_angles else "not "
print(f"The triangle is {valid}valid!")  # Refactor the output