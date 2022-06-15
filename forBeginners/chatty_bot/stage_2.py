#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Chatty bot project - Stage 2 ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Chatty bot project: Stage 2 ".center(80, "*"))
print(separator.center(80)+"\n")

# Description
# The greeting part is great, but chatbots are also supposed to interact with 
# a user. It's time to implement this functionality.
#
# Objective
# At this stage, you will introduce yourself to the bot so that it can greet 
# you by your name. 
#
# Your program should print the following lines:
#
#   Hello! My name is {bot_name}.
#   I was created in {birth_year}.
#   Please, remind me your name.
#   What a great name you have, {your_name}!

print("Hello! my name is Ro.")
print("I was created in 2000.")
user_name = input("Please, remind me your name.\n")
print("What a great name you have, " + user_name + "!")