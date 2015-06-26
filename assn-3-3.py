__author__ = 'kleung'

"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error.
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit.
For the test, enter a score of 0.85. 
"""

MAX_GRADE = 1.0
MIN_GRADE = 0.0

def letter_grade(grade):
    letter = "should be replaced"
    if grade > MAX_GRADE or grade < MIN_GRADE:
        raise ValueError("Invalid input. {0} is out of range.".format(grade))
    elif grade >= 0.9:
        letter = "A"
    elif grade >= 0.8:
        letter = "B"
    elif grade >= 0.7:
        letter = "C"
    elif grade >= 0.6:
        letter = "D"
    else:
        letter = "F"
    return letter

grade = float(input("Enter grade (between {0} to {1}): ".format(MIN_GRADE, MAX_GRADE)))

try:
    print(letter_grade(grade))
except ValueError as err:
    print(err)