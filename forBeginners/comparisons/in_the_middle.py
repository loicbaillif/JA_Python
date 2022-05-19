# Basic Data Types and Operations #
# Write a program that reads an integer value from input and checks 
# if it is less than 10 or greater than 250

low_limit = 10
high_limit = 250
user_input = int(input())
print(user_input < low_limit or user_input > high_limit)