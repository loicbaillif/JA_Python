#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Invoking a function: Exercise - Longest word ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Invoking a function: Exercise - Longest word")

# Find the longest word in a pair and print its length.

word1 = input()
word2 = input()

if len(word1) >= len(word2):
    print(len(word1))
else:
    print(len(word2))


print_title("End of exercise")


