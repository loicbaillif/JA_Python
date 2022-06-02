#  ******** JetBrains Academy - Python for Beginners ********
#  ****** IF statement ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" IF statement ".center(80, "*"))
print("_"*40+"\n\n")
print(" 1) Simple IF statement ".center(60, "#"))
# Indentation is all we need to identify blocks:
biscuits = 1
minimum_biscuits = 5
print("Let's check stock...")
if biscuits >= minimum_biscuits:
    print("Time for Tea")
    print("With a cloud of milk?")
print("See you tomorrow")

print("_"*30+"\n")
print(" 2) Nested IF statement ".center(60, "#"))
rainbow = "red, orange, yellow, green, blue, indigo, violet"
warm_colours = "red, yellow, orange"
my_colour = "orange"
if my_colour in rainbow:
    print("Wow! your colour is in the rainbow")
    if my_colour in warm_colours:
        print("Oh by the way, it's a warm colour")
    
