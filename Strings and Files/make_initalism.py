# Write a makeInitialism function that allows the user to enter a phrase, and then
# displays the first letters of the words in capitals for that phrase. For example, if the
# user enters “University of Portsmouth”, the function should display UOP.

def makeInitialism(phrase):
    wordArray = phrase.split()
    outputArray = ""
    for word in wordArray:
        outputArray+=word[0].upper()
    return outputArray
    
print(makeInitialism("University of Portsmouth"))