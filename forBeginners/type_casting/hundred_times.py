#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Type casting: Exercise - Exactly 100 times ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Type casting: Exercise - Exactly 100 times")


# https://hyperskill.org/learn/step/6716
# Jane knows that the variable n stores some integer number (for example, 
# 12345) and wants to print it exactly 100 times in one line. Help her and 
# write down a single line of code that will print number n exactly 100 times.

n = int(input())
print(str(n) * 100)

print_title("End of exercise")