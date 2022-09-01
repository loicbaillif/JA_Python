#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Loan calculator project - Stage 3 ******

# Global Python library import


separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Loan calculator project: Stage 3 ".center(80, "*"))
print(separator.center(80)+"\n")

# DESCRIPTION
# See the project page: https://hyperskill.org/projects/90/stages/502/implement


# FUNCTIONS
def get_secondary_inputs(user_main_choice):
    global p_loan 
    global a_loan
    global n_loan
    global i_loan
    if user_main_choice != "p":
        p_loan = input(f"Enter the {inputs_dict['p']}\n> ")
    if user_main_choice != "a":
        a_loan = input(f"Enter the {inputs_dict['a']}\n> ")
    if user_main_choice != "n":
        n_loan = input(f"Enter the {inputs_dict['n']}\n> ")
    i_loan = input(f"Enter the {inputs_dict['i']}\n> ")
    




# VARIABLES
main_menu = """What do you want to calculate?
type "n" for number of monthly payments, 
type "a" for annuity/monthly payment amount, 
type "p" for loan principal:
> """
inputs_dict = {
    "p": "loan principal", 
    "a": "monthly payment", 
    "n": "number of periods", 
    "i": "loan interest"}


# MAIN PROGRAM
user_main_choice = input(main_menu)
get_secondary_inputs(user_main_choice)