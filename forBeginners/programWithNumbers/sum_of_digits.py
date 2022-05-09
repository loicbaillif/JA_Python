# ****** Python for Beginners - Program with numbers ******
# ****** Exercise : The Sum of Digits ******
#
# Given a three-digit integer (i.e., an integer from 100 to 999), 
# find the sum of its digits and print the result.
#
# To get the separate digits of the input integer, make use of % and // 
# (for example, you can get 8 from the number 508 by taking the remainder 
# of the division by 10).

user_input = int(input("Enter a three-digit integer/n"))
units = user_input % 10
tenths = (user_input // 10) % 10
hundreds = user_input // 100
print("Units = ", units)
print("Tenths = ", tenths)
print("Hundreds = ", hundreds)
print(units + tenths + hundreds)
