#  ******** JetBrains Academy - Python for Beginners ********
#  ****** String Formatting: Exercise - Tax brackets ******


# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("String Formatting: Exercise - Tax brackets")


# https://hyperskill.org/learn/step/6519
# In progressive tax systems, tax rates change according to the income. 
# Tax brackets are divisions that regulate those changes.
# Here's an example of tax brackets in a certain tax system:
#       - 0 — 15,527: 0% tax
#       - 15,528 — 42,707: 15% tax
#       - 42,708 — 132,406: 25% tax
#       - 132,407 and more: 28% tax
# 
# Suppose we use a simplified version of taxation and apply one tax rate 
# to the entire amount of money.
# Write a program that calculates the tax that a person's going to pay 
# based on their income.
#
# The input format:
#   The value of someone's taxable income (in dollars).
# The output format:
#   The tax for {income} is {percent}%. That is {calculated_tax} dollars!
# 
# Round your calculated_tax to the nearest integer.


def get_tax_rate(income):
    tax_rate = 0
    if income > 132406:
        tax_rate = 28
    elif income > 42707:
        tax_rate = 25
    elif income > 15527:
        tax_rate = 15
    return tax_rate


income = int(input())
print(f"the tax for {income} is {get_tax_rate(income)}%. That is {round(get_tax_rate(income) * income / 100)} dollars!")

print_title("End of exercise")