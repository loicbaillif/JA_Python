#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Chatty bot project - Stage 3 ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Chatty bot project: Stage 3 ".center(80, "*"))
print(separator.center(80)+"\n")

# Description
# Keep improving your bot by developing new skills for it. We suggest a simple 
# guessing game that will predict the age of a user.
#
# It's based on a simple math trick. First, take a look at this formula:
#   age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
#       The numbersremainder3, remainder5 and remainder7 are the remainders of 
#       division by 3, 5 and 7 respectively.
#
# It turns out that for each number ranging from 0 to 104 the calculation will 
# result in the number itself. This perfectly fits the ordinary age range, 
# doesn't it? Ask a user for the remainders and use them to guess the age!

print("Hello! my name is Ro.")
print("I was created in 2000.")
user_name = input("Please, remind me your name.\n")
print(f"What a great name you have, {user_name}!\nLet me guess your age.")
print("Please answer the following 3 questions:")
remainder_3 = int(input("Enter the remainder of dividing your age by 3:\n> "))
remainder_5 = int(input("Enter the remainder of dividing your age by 5:\n> "))
remainder_7 = int(input("Enter the remainder of dividing your age by 7:\n> "))
age = (remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming")

