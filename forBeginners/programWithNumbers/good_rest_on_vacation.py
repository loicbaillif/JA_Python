# Program with Numbers #
# Write a program that will help people who are going on vacation. 
# The program should calculate the total required sum (e.g. $) of money 
# to have a good rest for a given duration.
#
# There are four parameters that have to be considered:
#   . duration in days
#   . total food cost per day
#   . one-way flight cost 
#   . cost of one night in a hotel (the number of nights is equal to the 
#     duration of days minus one)
#
# Read integer values of these parameters from the standard input and 
# then print the result.

duration_in_days = int(input("Duration in days?\n"))
food_per_day = int(input("Total food cost per day?\n"))
one_way_flight = int(input("One-way flight cost?\n"))
one_night_cost = int(input("How much for one night in a hotel?\n"))

print((duration_in_days - 1) * (food_per_day + one_night_cost) + 
one_way_flight * 2 + food_per_day)