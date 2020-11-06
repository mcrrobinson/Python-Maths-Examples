# A teacher awards letter grades for test marks as follows: 8, 9 or 10 marks give an A, 6
# or 7 marks give B, 4 or 5 marks give C, and 0, 1, 2 or 3 marks all give F. Using string
# indexing, write a function gradeTest which asks the user for a mark (between 0 and
# 10) and displays the corresponding grade.

grade_boundaries = {
    10:"A",
    9:"A",
    8:"A",
    7:"B",
    6:"B",
    5:"C",
    4:"C",
    3:"F",
    2:"F",
    1:"F",
    0:"F"
}

def gradeTest(mark):
    return grade_boundaries[mark]

print(gradeTest(5))