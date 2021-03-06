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


print("\n***** Keywords \"nonlocal\" and \"global\"")
print("1) global")
print("*** Example 1:")
x = 1
def print_global():
    print(x)

print_global()  # --> 1

def modify_global():
    print(x)
    #  x = x + 1 --> This causes an UnboundLocalError

modify_global()

print("*** Example 2:")
y = 1
def modify_global_y():
    global y
    print(y)
    y = y + 1
modify_global_y()
modify_global_y()
modify_global_y()

print("2) nonlocal")
def func():
    x = 1
    def inner():
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)

def nonlocal_func():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)

func()  # inner: 2
        # outer: 1

nonlocal_func()  # inner: 2
                 # outer: 2


print("_"*40+"\n\n")