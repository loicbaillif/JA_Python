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




print()
print_title("End of chapter")