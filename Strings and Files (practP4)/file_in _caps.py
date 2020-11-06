import os.path
# Write a fileInCaps function which displays the contents of a file in capital letters.
# The name of the input file should be entered by the user.

def fileInCaps(textFileName):
    structuredFileName = textFileName+".txt"
    if os.path.isfile(structuredFileName):
        stringStream = open(structuredFileName, "r")
        return stringStream.read().upper()
    return "File doesn't exist."

print(fileInCaps("file_in_caps"))