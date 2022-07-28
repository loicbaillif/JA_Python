#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - Menu ******

# Let's say you were asked to create a program for a restaurant: 
# a visitor enters what kind of food they would like to order and gets 
# back the restaurant's offer.
# The restaurant has just opened so its menu contains only a few options:
#   . pizza: Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy
#   . salad: Caesar salad, Green salad, Tuna salad, Fruit salad
#   . soup: Chicken soup, Ramen, Tomato soup, Mushroom cream soup
# If the visitors ask for something that is not on the menu, the program should write "Sorry, we don't have it on the menu".


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - Menu")

pizza = "Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy"
salad = "Caesar salad, Green salad, Tuna salad, Fruit salad"
soup = "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"
not_on_menu = "Sorry, we don't have it on the menu"

visitor_order = input()
if visitor_order == "pizza":
    print(pizza)
elif visitor_order == "salad":
    print(salad)
elif visitor_order == "soup":
    print(soup)
else:
    print(not_on_menu)
