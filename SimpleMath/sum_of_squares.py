def sumOfSquares(n):
    """ sumOfSquares

    Output the sum of the first n positive integers, where 
    n is provided by the user.

    passes:
        n:
            Output the sum of the first n positive integers, where 
            n is provided by the user.
    
    returns:
        Returns an array of the sum of the nth squared integers.
    """
    sumVars = []
    for x in range(1,n+1):
        sumVars.append(x**2)
    return sumVars

print(sumOfSquares(10))