def averageOfNumbers():
    """ averageOfNumbers

    Outputs the average of a series of numbers entered by the user.
    
    returns:
        The average of the numbers input by the user.
    """
    numbers = []
    amount_of_numbers = input("How many numbers do you wish to input? ")
    for x in range(1, int(amount_of_numbers)+1):
        entered_number = int(input("%d. Enter a number: "%(x)))
        numbers.append(entered_number)
    return sum(numbers) / len(numbers) 

print(averageOfNumbers())