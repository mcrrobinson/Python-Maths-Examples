# Write a formalName function which asks the user to input his/her given name and
# family name, and then outputs a more formal version of their name. E.g. on input
# Sam and Brown, the function should output S. Brown (again note the spacing and
# punctuation).

def formalName():
    fullname = input("Please enter your full name: ")
    return (fullname.split()[0][0]).title() + ". " + (fullname.split()[1]).title()

print(formalName())