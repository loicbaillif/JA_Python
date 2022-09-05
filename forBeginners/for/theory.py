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

for _ in range(3):
    print(">_</\<_>")


print_subtitle("Input data processing")
user_word = input()
for letter in user_word:
    print(letter)

nb_reps = int(input("How many guests do we have?"))
for _ in range(nb_reps):
    print("Welcome! Be my guest.")


print_subtitle("Nested loops")
first_names = ["Andy", "Betty"]
last_names = ["Alpha", "Bravo"]
for first_name in first_names:
    for last_name in last_names:
        print(first_name + " " + last_name)




print_title("End of chapter")