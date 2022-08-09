#  ******** JetBrains Academy - Python for Beginners ********
#  ****** elif statement: Exercise - The farm ******

# 

# Local application imports
from print_title import print_title

print_title("JetBrains Academy - Python for Beginners")
print_title("elif statement: Exercise - Grade")

# There are a number of grades you can get in a test: A, B, C, D, F. 
# The percentages are as follows:
#   A: 90-100%
#   B: 80-90%
#   C: 70-80%
#   D: 60-70%
#   F: <60%
# 
# Determine the grade that a student will get based on the student's 
# score and the maximum score.
#
# Note that the upper limit is not included in the range, except for the A
# grade. For example, a student with 60% will get D, with 70% or 79.9% — C, 
# but the top score 100% is just A.


# Variables
A_GRADE = 90
B_GRADE = 80
C_GRADE = 70
D_GRADE = 60
F_GRADE = 0
grades_dict = {
    'A': A_GRADE, 
    'B': B_GRADE, 
    'C': C_GRADE, 
    'D': D_GRADE, 
    'F': F_GRADE
}

# functions
def get_grade(student_grade):
    for x in grades_dict:
        if student_grade > grades_dict[x]:
            return x


# Tests
grades_test = (100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50)
for test in grades_test:
    print(get_grade(test))


print_title("End of exercise")