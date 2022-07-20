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