#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Loan calculator project - Stage 2 ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Loan calculator project: Stage 1 ".center(80, "*"))
print(separator.center(80)+"\n")

# DESCRIPTION
# Let's consider 0% interest loans. We will also round all monthly payment, to 
# get rid of cents.
# It is also important to remember that no payment can be more than the fixed 
# monthly payment.

# OBJECTIVES
# The behavior of your program should look like this:
#       - Prompt a user to enter their loan principal and choose which of the 
#       two parameters they want to calculate – the number of monthly payments 
#       or the monthly payment amount.
#       - To perform further calculations, you'll also have to ask for the 
#       required missing value.
#       - Finally, output the results for the user.

ask_input1 = "Enter the loan principal:\n"
ask_input2 = ("What do you want to calculate?\n\ttype 'm' - for number of "
    "monthly payments\n\ttype 'p' for the monthly payment:\n")
ask_input3 = ["m", "p"]
ask_input4 = ["Enter the monthly payment:\n", "Enter the number of months:\n"]

loan_principal = int(input(ask_input1))
user_choice = input(ask_input2)
additional_data = int(input(ask_input4[ask_input3.index(user_choice)]))

print(f"additional data = {additional_data}")

