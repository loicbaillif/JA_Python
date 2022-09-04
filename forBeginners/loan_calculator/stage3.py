#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Loan calculator project - Stage 3 ******

# Global Python library import
from math import ceil, floor, log


separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Loan calculator project: Stage 3 ".center(80, "*"))
print(separator.center(80)+"\n")

# DESCRIPTION
# See the project page: https://hyperskill.org/projects/90/stages/502/implement


# *** FUNCTIONS
def get_secondary_inputs(user_main_choice):
    global p_loan 
    global a_loan
    global n_loan
    global i_loan
    if user_main_choice != "p":
        p_loan = float(input(f"Enter the {inputs_dict['p']}\n> "))
    if user_main_choice != "a":
        a_loan = float(input(f"Enter the {inputs_dict['a']}\n> "))
    if user_main_choice != "n":
        n_loan = float(input(f"Enter the {inputs_dict['n']}\n> "))
    i_loan = float(input(f"Enter the {inputs_dict['i']}\n> ")) / 12 / 100
    

def calculate_a():
    a = p_loan * (i_loan * (1 + i_loan) ** n_loan) 
    a /= (( 1 + i_loan) ** n_loan - 1)
    print(f"Your monthly payment = {ceil(a)}!")


def calculate_n():
    n = log(a_loan / (a_loan - i_loan * p_loan), 1 + i_loan)
    print(format_years_months(ceil(n)))  # Number of months ==> ceil


def calculate_p():
    p = a_loan / ((i_loan * (1 + i_loan) ** n_loan) / ((1 + i_loan) ** n_loan - 1))
    print(f"Your loan principal = {floor(p)}!")


def format_years_months(total_months):
    nb_years = total_months // 12
    nb_months = total_months % 12
    f_years = "" if (nb_years == 0) else ("{} {} ".format(
        nb_years, singular_plural("year", nb_years)))
    f_months = "" if (nb_months == 0) else ("{} {} ".format(
        nb_months, singular_plural("month", nb_months)))
    optional_and = "" if (f_years == "" or f_months == "") else "and "
    return f"It will take {f_years}{optional_and}{f_months}to repay this loan!"


def treat_request(user_choice):
    if user_choice == "a":
        calculate_a()
    elif user_choice == "n":
        calculate_n()
    elif user_choice == "p":
        calculate_p()
    else:
        print("This request cannot be treated")


def singular_plural(word, qty):
    return word if qty < 2 else (word + "s")



# *** VARIABLES
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


# *** MAIN PROGRAM
user_main_choice = "dummy"
while user_main_choice not in ["n", "a", "p"]:
    print("Invalid input, please try again")
    user_main_choice = input(main_menu)
get_secondary_inputs(user_main_choice)
treat_request(user_main_choice)


# TESTS
# print(calculate_a())
# print(calculate_p())
# print(calculate_n())
# test_format_months = [1, 3, 12, 13, 20, 24, 36, 49, 100]
# for x in test_format_months:
#     print(format_years_months(x))