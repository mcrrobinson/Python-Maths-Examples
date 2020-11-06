import os.path

# function: rainfallInInches
    
#     [harder] Write a rainfallInInches function that reads the rainfall data from rainfall.txt, and outputs the data to a file rainfallInches.txt where all the mm values are
#     converted to inches (there are 25.4mm in an inch). The inch values should be given
#     to two decimal places, so the Portsmouth line above will become:
#         Portsmouth      0.35

def rainfallChart():
    structuredFileName = "rainfall.txt"
    outputtedString = ""
    if os.path.isfile(structuredFileName):
        stringStream = open(structuredFileName, "r")
        for line in stringStream.readlines():
            parser=line.split()
            outputtedString+="%s    \t%s inches\n"%(parser[0],round(int(parser[1])/25.4, 2))
        return outputtedString
    return "File doesn't exist."

print(rainfallChart())