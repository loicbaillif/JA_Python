#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - Recommender ******

# Write a program that recommends one of the following movies based on the age of a user:

#     <=16: "Lion King"

#     17 - 25: "Trainspotting"

#     26 - 40: "Matrix"

#     41−60: "Pulp Fiction"

#     >60: "Breakfast at Tiffany's"

# The user enters their age and the program outputs one title.


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - Recommender")

user_age = int(input())
if user_age <= 16:
    recommendation = "Lion King"
elif user_age <= 25:
    recommendation = "Trainspotting"
elif user_age <= 40:
    recommendation = "Matrix"
elif user_age <= 60:
    recommendation = "Pulp Fiction"
else:
    recommendation = "Breakfast at Tiffany's"

print(recommendation)