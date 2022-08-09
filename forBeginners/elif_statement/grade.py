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



# Alternative solution
student_score_percentage = convert_score(student_score, max_score)
if student_score_percentage >= 90:
    print('A')
elif student_score_percentage >= 80:
    print('B')
elif student_score_percentage >= 70:
    print('C')
elif student_score_percentage >= 60:
    print('D')
else:
    print('F')


print_title("End of exercise")