# [harder] Write a nameToNumber function that asks the user for their name and converts
# it into a numerical value by adding up the “values” of its letters (where ‘a’ is 1, ‘b’ is
# 2, . . . ‘z’ is 26). So, for example, “Sam” has the value 19 + 1 + 13 = 33.

def nameToNumber(name):
    sumOfName = 0
    for i in name.lower():
        sumOfName += ord(i)-96
    return sumOfName

print(nameToNumber("Sam"))