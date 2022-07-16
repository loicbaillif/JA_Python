#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Scope: Theory ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Scope: Theory ".center(80, "*"))
print("_"*40+"\n\n")

print("***** Global VS Local")

phrase = "Let it be"  # Global variable

def global_printer():
    print(phrase)  # we can call variable phrase because it's global

global_printer()  # --> "Let it be"
print(phrase)  # Works as well because we call global variable from global zone

phrase = "Hey Jude"

global_printer()  # --> "Hey Jude" because variable value was changed 

def local_printer():
    local_phrase = "Yesterday"
    print(local_phrase)

local_printer()  # --> "Yesterday"
# print(local_phrase)  # Impossible, causes NameError



print("_"*40+"\n\n")