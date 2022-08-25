#  ******** JetBrains Academy - Python for Beginners ********
#  ****** String Formatting: Theory ******


# Local application imports
from print_title import print_title
from print_title import print_subtitle

print_title("JetBrains Academy - Python for Beginners")
print_title("String Formatting")

print_subtitle("The str.format() method")
print("Mix {}, {} and a {} to make an ideal omelet".
        format("2 eggs", "30g of milk", "pinch of salt"))

print("{0} in the {1}, by Frank Sinatra".format("Strangers", "Night"))
print("{1} in the {0}, by Frank Sinatra".format("Strangers", "Night"))
print("{1} in the {0}, by Frank Sinatra".format("Night", "Strangers"))

print("The {movie} movie at {theatre} was {adjective}.".
        format(movie="Mad Max: Fury Road", 
               adjective="insane", 
               theatre="Gaumont Champs-Elysées"))


print_subtitle("Formatted string literals")
name = "Elizabeth II"
title = "Queen of the United Kingdom and the other Commonwealth realms"
reign = "the longest-lived and the longest-reigning British monarch"
print(f"{name}, the {title}, is {reign}.")

bottle_price_in_cents = 2895
bottle_name = "Chateau Latour"
print(f"The {bottle_name} costs {bottle_price_in_cents / 100:.2f}€.")

invite1 = "Please enter an integer number:\n> "
invite2 = "Please enter the percentage you want from {}:\n> "
invite3 = "Please enter the required number of decimals:\n> "
hundred_percent_number = float(input(invite1))
required_percentage = int(input(invite2.format(hundred_percent_number)))
required_precision = int(input(invite3))
user_result = hundred_percent_number * (required_percentage / 100.0)
print((f"{required_percentage}% of {hundred_percent_number} "
        f"(with {required_precision} digits) " 
        f"equals {user_result:.{required_precision}f}"))


print()
print_title("End of chapter")