#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Math functions: Exercise - Heron's formula ******

# Global Python import
import math

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Math functions - Exercise: Heron's Formula")

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)


print_title("End of exercise")