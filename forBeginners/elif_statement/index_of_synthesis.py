#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - Index of synthesis ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - Calculator")

# https://hyperskill.org/learn/step/6533
# One way to classify the languages of the world is by looking at their
# morphological systems. One classification is based on the index of
# synthesis that reflects the average number of morphemes in a word.
# The values vary between 1 and 4 and there are 3 types of languages
# according to that system. Here they are:
#
#   Type — Index
#   Analytic — less than 2
#   Synthetic — from 2 to 3 (inclusively)
#   Polysynthetic — more than 3
#
# Write a program that given the index of synthesis determines the type of the language.
#
# The input format:
#   The value of the index of synthesis.
# The output format:
#   The type of language.

index_synthesis = float(input())
if index_synthesis < 2:
    print("Analytic")
elif index_synthesis <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")


print_title("End of exercise")