#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Declaring a function: Exercise - Fahrenheit ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("Declaring a function: Exercise - Fahrenheit")

# Convert the temperature from Fahrenheit to Celsius in the function below. 
# You can use this formula:
#
#       C° = (F° - 32) * 5 / 9 
# 
# Round the returned result to 3 decimal places.


def fahrenheit_to_celsius(temperature):
    temp_celsius = (temperature - 32) * 5 / 9
    return round(temp_celsius, 3)



print_title("End of exercise")