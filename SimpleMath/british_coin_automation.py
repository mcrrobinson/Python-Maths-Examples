import math
from functools import reduce


def selectCoins(init_value = 292):
    """ sumOfSquares

    Asks the user to enter an amount of money (in pence) 
    and then outputs the number of coins of each denomination 
    (from £2 down to 1p) that should be used to make up that
    amount exactly (using the least possible number of coins).

    passes:
        init_value:
            The number of pennies the user has.
    
    returns:
        Those pennies sorted into most significant coin factor.
    """
    two_pounds = (init_value - (init_value % 200))
    init_value = init_value - two_pounds

    one_pound = (init_value - (init_value % 100))
    init_value = init_value - one_pound

    fifty_pence = (init_value - (init_value % 50))
    init_value = init_value - fifty_pence

    twenty_pence = (init_value - (init_value % 20))
    init_value = init_value - twenty_pence

    ten_pence = (init_value - (init_value % 10))
    init_value = init_value - ten_pence

    five_pence = (init_value - (init_value % 5))
    init_value = init_value - five_pence

    two_pence = (init_value - (init_value % 2))
    init_value = init_value - two_pence

    one_pence = (init_value - (init_value % 1))
    init_value = init_value - one_pence
    return [two_pounds, one_pound, fifty_pence, twenty_pence, ten_pence, five_pence, two_pence, one_pence]

x = selectCoins(18923)
print("£2: %d| £1: %d| 50p: %d| 20p: %d| 10p: %d| 5p: %d| 2p: %d| 1p: %d"%(
        x[0]/200, 
        x[1]/100, 
        x[2]/50, 
        x[3]/20, 
        x[4]/10, 
        x[5]/5, 
        x[6]/2, 
        x[7]/1
    )
)