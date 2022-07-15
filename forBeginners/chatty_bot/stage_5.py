#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Chatty bot project - Stage 4 ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Chatty bot project: Stage 4 ".center(80, "*"))
print(separator.center(80)+"\n")

# DESCRIPTION
# At the final stage, you will improve your simple bot so that it can give you 
# a test and check your answers. The test should be a multiple-choice quiz 
# about programming. Your bot has to repeat the test until you answer 
# correctly and congratulate you upon completion.
#
# OBJECTIVE
# Your bot can ask anything you want, but there are two rules for your output:
#   -> The line with the test should end with the question mark character;
#   -> An option starts with a digit followed by the dot (1., 2., 3., 4.);
# If a user enters an incorrect answer, the bot may print a message:
#   "Please, try again."
# The program should stop on the correct answer and print 
# "Congratulations, have a nice day!" at the end.


print("Hello! my name is Rob.")
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
max_count = int(input("> "))
i = 0
while i <= max_count:
    print(f"{i} !")
    i += 1
print("Completed, have a nice day!")
