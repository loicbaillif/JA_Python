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

nb_bears = int(input("What is the maximum number of bears\n> "))
poem1 = " little bear"
poem2 = "Wondering what to do"
poem3 = "Along came another"
poem4 = "Then there were"

for i in range(1, nb_bears):
    print(i, poem1, '' if i == 1 else 's', sep='')
    print(poem2)
    print(poem3)
    print(poem4, i + 1)



print_title("End of exercise")