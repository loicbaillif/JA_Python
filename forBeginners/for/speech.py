#  ******** JetBrains Academy - Python for Beginners ********
#  ****** for loop: Exercise - Speech generation ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("for loop: Exercise - Speech generation")

# https://hyperskill.org/learn/step/8438
# Here is your chance to write instructions for a text-to-speech system. 
# Let's focus on reading phone numbers aloud. The input phone number will 
# consist solely of digits. Print the name of each digit on a new line for 
# the system to read them one by one.

digits_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

number = input()
for digit in number:
    print(digits_words[int(digit)])

print_title("End of exercise")