#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - What day is it? ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - What day is it?")


# We consider the followings:
#   - The reference time point is Tuesday, 10:30 in the morning 
#     in London (UTC+00:00)
#   - Read the input string containing the number and the sign of this 
#     number (for example, +4, -10). Note, however, that there will be no sign 
#     if the number is 0. The number is always an integer.
#   - This number is the offset for some time zone.
#   - Your program should calculate the day of the week in the time zone for 
#     which you were given the offset. The reference time point for your 
#     calculations is mentioned above.
#   - Output the day of the week in the given time zone.
#
# The input format:
#   The value of offset with the sign (e.g. +3 or -9). 
#
# The output format:
#   The day of the week in that timezone.

reference_time = 10.5  # 10:30 at London
timezone_day_of_week = ["Tuesday", "Wednesday", "Monday"]
timezone = reference_time + int(input())
timezone_day = int(timezone // 24)  # will return -1, 0 or 1

print(timezone_day_of_week[timezone_day])
