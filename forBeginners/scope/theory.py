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

print("\n***** LEGB rule")
print("Python interpreter will look for variables in following order:")
print("Local --> Enclosing --> Global --> Built-in")

print("*** Example 1:")
x = "global"
def outer_x():
    x = "outer local"
    def inner_x():
        x = "inner local"
        def func_x():
            x = "func local"
            print(x)
        func_x()
    inner_x()

outer_x()  # --> "func local"

print("*** Example 2:")
y = "global"
def outer_y():
    y = "outer local"
    def inner_y():
        y = "inner local"
        def func_y():
            print(y)
        func_y()
    inner_y()

outer_y()  # --> inner_local

print("*** Example 3:")
z = "global"
def outer_z():
    def inner_z():
        def func_z():
            print(z)
        func_z()
    inner_z()

outer_z()  # --> global





print("_"*40+"\n\n")