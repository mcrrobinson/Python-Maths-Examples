# Suppose the University decides that students’ email addresses should be made up of
# the first 4 letters of their surname, the first letter of their forename, and the final
# two digits of the year they entered the university, separated by dots. Write a function
# called generateEmail that outputs an email address given a student’s details. (E.g., if
# the user enters the following information: Sam, Brown and 2020, the function should
# output: brow.s.20@myport.ac.uk

def generateEmail(firstname, secondname, year):
    return (secondname[:4] + "." + firstname[0] + "." + str(year) + "@myport.ac.uk").lower()

print(generateEmail("Matt", "Robinson", 2020))
