#  ******** JetBrains Academy - Python for Beginners ********
#  ****** String Formatting: Exercise - Film ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("String Formatting: Exercise - Film")


# Write a program that gets information about a movie from the input 
# and presents in the following format:
#   movie (dir. director) came out in year XXXX
#
# The input format:
#   3 lines: first the title of the movie, then the name of the director 
#   and then the year of its release.

movie_title = input("Please enter the movie title:\n> ")
movie_director = input("Please enter the movie directir:\n> ")
movie_release_year = input("Please enter the movie release year:\n> ")

print(f"{movie_title} (dir. {movie_director}) "
      f"came out in {movie_release_year}")


print_title("End of exercise")