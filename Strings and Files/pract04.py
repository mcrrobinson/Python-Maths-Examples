import os.path

# Globals
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

def personalGreeting(username):
    """
    function: personalGreeting

    Write a personalGreeting function which, after asking for the user’s name, outputs a
    personalised greeting. E.g., for user input Sam, the function should output the 
    greeting Hello Sam, nice to see you! (note the details of the spaces and punctuation).
    """
    return "Hello "+username+", nice to meet you."

def formalName(fullname):
    """ 
    function: formalName

    Write a formalName function which asks the user to input his/her given name and
    family name, and then outputs a more formal version of their name. E.g. on input
    Sam and Brown, the function should output S. Brown (again note the spacing and
    punctuation).
    """
    return (fullname.split()[0][0]).title() + ". " + (fullname.split()[1]).title()

def pounds2kilos(poundValue):
    """
    function: pounds2kilos

    Copy the kilos2pounds conversion function from your pract01.py file. Modify this
    function so that its output takes the form of a message such as “12.34 kilos is equal
    to 27.15 pounds”, where both the user’s kilos value and the calculated pounds values
    are displayed to two decimal places.
    """
    return round(poundValue / 2.25,2)

def kilos2pounds(kiloValue):
    """
    function: kilos2pounds

    Copy the kilos2pounds conversion function from your pract01.py file. Modify this
    function so that its output takes the form of a message such as “12.34 kilos is equal
    to 27.15 pounds”, where both the user’s kilos value and the calculated pounds values
    are displayed to two decimal places.
    """
    return round(kiloValue * 2.25,2)

def generateEmail(firstname, secondname, year):
    """
    function: generateEmail

    Suppose the University decides that students’ email addresses should be made up of
    the first 4 letters of their surname, the first letter of their forename, and the final
    two digits of the year they entered the university, separated by dots. Write a function
    called generateEmail that outputs an email address given a student’s details. (E.g., if
    the user enters the following information: Sam, Brown and 2020, the function should
    output: brow.s.20@myport.ac.uk
    """
    return (secondname[:4] + "." + firstname[0] + "." + str(year) + "@myport.ac.uk").lower()

def gradeTest(mark):
    """
    function: gradeTest

    A teacher awards letter grades for test marks as follows: 8, 9 or 10 marks give an A, 6
    or 7 marks give B, 4 or 5 marks give C, and 0, 1, 2 or 3 marks all give F. Using string
    indexing, write a function gradeTest which asks the user for a mark (between 0 and
    10) and displays the corresponding grade.
    """
    return grade_boundaries[mark]

def singASong(word, y, x):
    """
    function: singASong

    Write a singASong function which outputs a “song” based on a single word. The user
    should be asked for the song’s word, how many lines long the song should be, and
    how many times the word should be repeated on each line. For example, if the user
    enters the word “dum” and the numbers 2 and 4, the function should then output the
    following song (note that the spaces are important):
    dum dum dum dum
    dum dum dum dum
    """
    stringStream = ""
    for i in range(y):
        string += (word+" ")*x+"\n"
    return stringStream

def exchangeTable(pounds):
    """
    function: exchangeTable

    Write a function exchangeTable that gives a table of euros values and their equivalent
    values in pounds, using an exchange rate of 1.10 euros to the pound. The euros values
    should be 0, 1, 2, . . . , 20, and should be right justified. The pounds values should be
    6
    right justified and given to two decimal places (i.e. with decimal points lined up and
    with pence values after the points).
    """
    return round(pounds * 1.1, 2)

def makeInitialism(phrase):
    """
    function: makeInitalisism

    Suppose the University decides that students’ email addresses should be made up of
    the first 4 letters of their surname, the first letter of their forename, and the final
    two digits of the year they entered the university, separated by dots. Write a function
    called generateEmail that outputs an email address given a student’s details. (E.g., if
    the user enters the following information: Sam, Brown and 2020, the function should
    output: brow.s.20@myport.ac.uk
    """
    wordArray = phrase.split()
    outputArray = ""
    for word in wordArray:
        outputArray+=word[0].upper()
    return outputArray

def nameToNumber(name):
    """
    function: nameToNumber

    [harder] Write a nameToNumber function that asks the user for their name and converts
    it into a numerical value by adding up the “values” of its letters (where ‘a’ is 1, ‘b’ is
    2, . . . ‘z’ is 26). So, for example, “Sam” has the value 19 + 1 + 13 = 33.
    """
    sumOfName = 0
    for i in name.lower():
        sumOfName += ord(i)-96
    return sumOfName

def fileInCaps(textFileName):
    """
    function: fileInCaps

    Write a fileInCaps function which displays the contents of a file in capital letters.
    The name of the input file should be entered by the user.
    """
    structuredFileName = textFileName+".txt"
    if os.path.isfile(structuredFileName):
        stringStream = open(structuredFileName, "r")
        return stringStream.read().upper()
    return "File doesn't exist."

def rainfallChart():
    """
    function: rainfallChart

    Write a function rainfallChart that displays this data as a textual bar chart using
    one asterisk for each mm of rainfall; e.g., given the above data the output should be:

        Portsmouth      ********
        London          *****
        Southampton     ************
    """
    structuredFileName = "rainfall.txt"
    outputtedString = ""
    if os.path.isfile(structuredFileName):
        stringStream = open(structuredFileName, "r")
        for line in stringStream.readlines():
            parser=line.split()
            outputtedString+="%s    \t%s\n"%(parser[0],"*"*int(parser[1]))
        return outputtedString
    return "File doesn't exist."

def rainfallInInches():
    """
    function: rainfallInInches
    
    [harder] Write a rainfallInInches function that reads the rainfall data from rainfall.txt, and outputs the data to a file rainfallInches.txt where all the mm values are
    converted to inches (there are 25.4mm in an inch). The inch values should be given
    to two decimal places, so the Portsmouth line above will become:
        Portsmouth      0.35
    """
    structuredFileName = "rainfall.txt"
    outputtedString = ""
    if os.path.isfile(structuredFileName):
        stringStream = open(structuredFileName, "r")
        for line in stringStream.readlines():
            parser=line.split()
            outputtedString+="%s    \t%s inches\n"%(parser[0],round(int(parser[1])/25.4, 2))
        return outputtedString
    return "File doesn't exist."

print(personalGreeting("Matt Robinson"))
print(formalName("Matthew Robinson"))
print("KGS: %s | LBS: %s"%(pounds2kilos(27.77), kilos2pounds(12.34)))
print(generateEmail("Matt", "Robinson", 2020))
print(gradeTest(5))
print(singASong("This is dumb",2,4))
print(exchangeTable(6))
print(makeInitialism("University of Portsmouth"))
print(nameToNumber("Sam"))
print(fileInCaps("file_in_caps"))
print(rainfallChart())
print(rainfallInInches())