#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Type casting: Exercise - Lexical reduplication ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Type casting: Exercise - Lexical Reduplication")


# https://hyperskill.org/learn/step/8213
# The languages of the world are amazing! Programming languages too, but now
# we will talk about the human ones. In linguistics, repeating a word or part
# of it is called reduplication. This morphological phenomenon is found in
# different languages. Think for a second, and you will definitely come up 
# with a couple of examples. Just to name a few: knock-knock, so-so, bye-bye.
#
# We have a full reduplication here since the entire word is repeated. That's 
# the mechanism we want you to implement. Print a word exactly 2 times. 
# The spelling rules vary across the globe, so do not separate the halves.

word = input()
print(word + word)

print_title("End of exercise")