#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Theory ******

# Local application imports
from print_title import print_title
from print_title import print_subtitle

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement")

print_subtitle("First example")
price = 10000  # some int value
if price > 5000:
    print("This is too expansive!")
elif price > 500:
    print("I can afford that.")
else:
    print("Not expansive enough, my son!")

print_subtitle("Second example")
pet = "dog"  # or "cat"?
# cats VS dogs solved for good:
if pet == "cat":
    print("Oh, you are a cat person. Meow!")
elif pet == "dog":
    print("Oh you are a dog person. Woof!")

print_subtitle("Multiple elifs and a decision tree")
light = "red"
if light == "green":
    print("You can go.")
elif light == "orange":
    print("You should brake now...")
elif light == "red":
    print("Just wait.")
else:
    print("No such traffic light colour. Do as you please.")

print_subtitle("Nested elif")
# rewrite here-above example:
traffic_lights = "green, orange, red"
if light in traffic_lights:
    if light == "green":
        print("You can go.")
    elif light == "orange":
        print("You should brake now...")
    else:
        # can only be red here ...
        print("Just wait")
else:
    print("No such traffic light colour. Do as you please.")

print_subtitle("Summary")
print("Even though we know only basic if ... elif ... else structure, ")
print("this is sufficient to create quite complex and complete programs.")