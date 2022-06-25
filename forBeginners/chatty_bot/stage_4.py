#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Chatty bot project - Stage 4 ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Chatty bot project: Stage 4 ".center(80, "*"))
print(separator.center(80)+"\n")

# Description
# Now you will teach your bot to count. It's going to become
# an expert in numbers!
#
# Objective
# At this stage, you will program the bot to count from 0 to any
# positive number users enter.

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
print("Now I will prove to you that I can count to any number you want")
max_count = int(input())
i = 0
while i <= max_count:
    print(f"{i} !")
    i += 1
print("Completed, have a nice day!")
