#  ******** JetBrains Academy - Python for Beginners ********
#  ****** While loop ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" While loop: Exercise - Rich Man's World ".center(80, "*"))
print(separator.center(80)+"\n")


# When a bank has financial problems the government can return a client's 
# deposit if it is less than 700,000. The interest rate for a particular 
# deposit is 7.1% a year. The percentages are paid to the same deposit at  
# the end of the year and a new value of the interest is calculated.
#
# Find out how many years it will take for the sum of the deposit to exceed 
# the value protected by the government.
#
# The input format:
#   The initial sum of the deposit. It is guaranteed that the value 
#   will be between 50,000 and 700,000.
#
# The output format:
#   The number of years.

deposit = int(input("What is the initial deposit value? (dollars)"))
protected_value = 700000
interest_rate = 1.071
nb_years = 0
while deposit < protected_value:
    deposit *= interest_rate
    nb_years += 1
print(nb_years)