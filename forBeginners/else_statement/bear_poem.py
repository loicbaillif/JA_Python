#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - The bear poem ******

# When you were a child, you must have loved poems for kids. Below is one 
# of them, its idea is the following: one bear thinks over what to do, then 
# comes another one and they think together. Then comes the third one, the 
# fourth one, etc. Here's the beginning of the poem:
#   One little bear
#   Wondering what to do
#   Along came another
#   Then there were two!
#
# Create a code that print the poem several times (user input), just changing
# the number of bears

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Else Statement - Exercise: The bear poem")

nb_bears = int(input())
i = 0
poem1 = "little bear\nWondering what to do"
poem2 = "Along came another\nThen there were"

for i in range(nb_bears):
    print(i + 1, poem1)
    print(poem2, i + 2)



print_title("End of exercise")