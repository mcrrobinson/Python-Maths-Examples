def fibonacci(n):
    """ fibonacci

    Asks the user for a number n and, using a loop, 
    calculates and outputs the n-th value in the Fibonacci sequence.

    passes:
        n:
            N is the number of iterations the fibonacci sequence
            goes through.
    
    returns:
        Returns the array of fibbonaci numbers.
    """
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
    
print(fibonacci(10))