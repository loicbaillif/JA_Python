#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Loan calculator project - Stage 2 ******

# Global Python library import
from math import ceil


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


# FUNCTIONS
def collect_input_array(invite, range):
    user_input = ""
    while (user_input not in range):
        user_input = input(invite)
    return user_input


def collect_int_greater_than(invite, min):
    # min included in authorized range
    user_input = min - 1
    while min > user_input:
        user_input = int(input(f"{invite} (greater or equal to {min}):\n"))
    return user_input


def print_string_number_months(principal, monthly):
    nb_months = ceil(principal / monthly)
    plural = 's' if (nb_months > 1) else ''
    print(output_nb_months.format(nb_months = nb_months, plural = plural))



# VARIABLES
ask_input1 = "Enter the loan principal:"
ask_input2 = ("What do you want to calculate?\n\ttype 'm' - for number of "
    "monthly payments\n\ttype 'p' for the monthly payment:\n")
ask_input3 = ["m", "p"]
ask_input4 = {
    "m": "Enter the monthly payment", 
    "p": "Enter the number of months"
}
output_nb_months = "It will take {nb_months} month{plural} to repay the loan"


# MAIN PROGRAM
loan_principal = collect_int_greater_than(ask_input1, 0)
user_choice = collect_input_array(ask_input2, ask_input3)
additional_data = collect_int_greater_than(ask_input4.get(user_choice), 0)

if user_choice == ask_input3[0]:
    print_string_number_months(loan_principal, additional_data)


print(f"additional data = {additional_data}")  # DEBUG: to be deleted

