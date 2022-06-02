#  ******** JetBrains Academy - Python for Beginners ********
#  ****** IF statement ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" IF statement: Exercise - Cook book".center(80, "*"))
print(separator.center(80)+"\n\n")

# Any recipe starts with a list of ingredients. # Below is an extract from a 
# cookbook with the ingredients for some dishes. Write a program that  
# tells you what recipe you can make based on the ingredient you have.

pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

user_input = input()

if user_input in pasta:
    print("pasta time!")
if user_input in apple_pie:
    print("apple pie time!")
if user_input in ratatouille:
    print("ratatouille time!")
if user_input in chocolate_cake:
    print("chocolate cake time!")
if user_input in omelette:
    print("omelette time!")
