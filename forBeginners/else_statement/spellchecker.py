#  ******** JetBrains Academy - Python for Beginners ********
#  ****** else statement - Exercise ******

print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" else statement: Exercise - Spellchecker ".center(80, "*"))
print("_"*40+"\n\n")

# Write a simple spellchecker that tells you if the word is spelled correctly. 
# Use the dictionary in the code below: it contains the list of 
# all correctly written words.

# The input format:
#   A single line with the "word".

# The output format:
#   If the word is spelled correctly write Correct, otherwise, Incorrect.

dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]

user_input = input("Please enter a word, its spelling will be checked:\n> ")

answer_tuple = ("Incorrect", "Correct")
print(answer_tuple[user_input in dictionary])