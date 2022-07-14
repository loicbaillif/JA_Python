#  ******** JetBrains Academy - Python for Beginners ********
#  ****** else statement ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" else statement: Exercise - Shortcuts ".center(80, "*"))
print("_"*40+"\n\n")

# Now let's rewrite this if-else statement. 
# It should produce the same result but in one line.


# Original:
print("Have you had enough hours of sleep today?")
answer = input()
# if answer == "yes":
#     print("Let's drink cocoa!")
# else:
#     print("I'd recommend a coffee!")

# Proposal
print("Let's drink cocoa!" if answer == "yes" else "I'd recommend a coffee!")