import os.path

# Write a function rainfallChart that displays this data as a textual bar chart using
# one asterisk for each mm of rainfall; e.g., given the above data the output should be:

#     Portsmouth      ********
#     London          *****
#     Southampton     ************

def rainfallChart():
    structuredFileName = "rainfall.txt"
    outputtedString = ""
    if os.path.isfile(structuredFileName):
        stringStream = open(structuredFileName, "r")
        for line in stringStream.readlines():
            parser=line.split()
            outputtedString+="%s    \t%s\n"%(parser[0],"*"*int(parser[1]))
        return outputtedString
    return "File doesn't exist."

print(rainfallChart())