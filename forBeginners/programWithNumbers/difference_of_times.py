# ****** Python for Beginners - Program with numbers ******
# ****** Exercise : Difference of times ******
#
# You will get the values for two moments in time of the same day: 
# when Megan went for a walk, and when it started to rain. 
# It is known that the first event happened earlier than the second one. 
# Find out how many seconds passed between them.
# 
# The program gets the input of six integers, each on a separate line. 
# The first three integers represent hours, minutes, and seconds of the first 
# event, and the rest three integers define similarly the second event. 
# Print the number of seconds between these two moments of time.

from_hours = int(input("Time you get out? (hours)"))
from_minutes = int(input("Time you get out? (minutes)"))
from_seconds = int(input("Time you get out? (seconds)"))
to_hours = int(input("Time you get back? (hours)"))
to_minutes = int(input("Time you get back? (minutes)"))
to_seconds = int(input("Time you get back? (seconds)"))

print(((to_hours - from_hours) * 60 + 
        to_minutes - from_minutes) * 60 + 
        to_seconds - from_seconds)  # Horner's method
