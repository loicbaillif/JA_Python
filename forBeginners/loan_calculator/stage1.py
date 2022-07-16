#  ******** JetBrains Academy - Python for Beginners ********
#  ****** Loan calculator project - Stage 1 ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" Loan calculator project: Stage 1 ".center(80, "*"))
print(separator.center(80)+"\n")

# DESRIPTION
# Let's think about what a loan calculator should be able to do. In general, 
# it takes several parameters like a loan principal and interest, calculates 
# the values the user wants to know (for example, monthly payment 
# or overpayment), and outputs them to the user.

# Not familiar with these concepts? Don't worry, we will explain them to you 
# in simple terms. The principal is the original amount of money you borrow. 
# The interest is a charge for borrowing that money, usually calculated as 
# a percentage of the principal amount.

# OBJECTIVES
# Let's start by imitating this behavior. There are some prepared variables in 
# the source code: these are text messages that our loan calculator can output.
# In this stage, all you need to do is output them in the right order.


loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'