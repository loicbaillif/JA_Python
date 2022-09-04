#  ******** JetBrains Academy - Python for Beginners ********
#  ****** For loop: Theory ******

# Global Python import


# Local application imports
from print_title import print_title
from print_title import print_subtitle

print_title("JetBrains Academy - Python for Beginners")
print_title("For loop")

print_subtitle("for loop syntax")
oceans = ["Arctic", "Atlantic", "Indian", "Pacific", "Southern"]
for ocean in oceans:
    print(ocean)

for letter in "Superbus":
    print(letter)


print_subtitle("range function")
for i in range(5):
    print(f"Counting ... {i}")

for i in range(7, 100, 15):
    print(f"Counting from 7 to 100 by steps of 15: {i}")

for _ in range(10):
    print("**********")


print_title("End of chapter")