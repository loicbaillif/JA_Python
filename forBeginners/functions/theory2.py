#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Declaring a function ******

from audioop import mul


print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Declaring a function: Theory ".center(80, "*"))
print("_"*40+"\n\n")

print(" First example ".center(60, "*"))
def multiply(x, y):
    return x * y

print(multiply(3, 4))
print(multiply(6, 3))

def praise():
    return "Of course you are the best!"

print(praise())
print(praise().center(50, "~"))

def give_up(random):
    pass

print(give_up(321))
print(give_up("AZERTY"))

print()
print(" Parameter VS Argument ".center(60, "*"))

def send_postcard(address, message):
    print("Sending a postcard to ", address)
    print("With the message: ", message)

send_postcard("Hilton, 97", "Hello, bro!")
# Sending a postcard to Hilton, 97
# With the message: Hello, bro!

send_postcard("Mafate", "N'arvu")
# Sending a postcard to Mafate
# With the message: N'arvu

# send_postcard("Sesame Street")
# Won't work - type error

print()
print(" Execution and return ".center(60, "*"))

def celsius_to_fahrenheit(temp_c):
    temp_f = temp_c * 9 / 5 +32
    return temp_f

# Examples:
water_bp = celsius_to_fahrenheit(100)  # return value stored in variable
print(f"Water boils at {water_bp} degrees Fahrenheit")
nothing = print("We will rock you")  # print does not return anything 
print(nothing)  # printing nothing gives "None"