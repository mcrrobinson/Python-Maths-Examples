# Copy the kilos2pounds conversion function from your pract01.py file. Modify this
# function so that its output takes the form of a message such as “12.34 kilos is equal
# to 27.15 pounds”, where both the user’s kilos value and the calculated pounds values
# are displayed to two decimal places.


def pounds2kilo(poundValue):
    return round(poundValue / 2.25,2)

def kilos2pounds(kiloValue):
    return round(kiloValue * 2.25,2)

print("KGS: %s | LBS: %s"%(pounds2kilo(27.77), kilos2pounds(12.34)))