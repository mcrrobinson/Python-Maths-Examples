import math
from functools import reduce


def selectCoins(init_value):
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
    amount_of_coins = {200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}
    for coin in list(amount_of_coins):
        amount_of_coins[coin] = (init_value - (init_value % coin))
        init_value = init_value - amount_of_coins[coin]
    return amount_of_coins

x = selectCoins(8934123)
print("£2: %d| £1: %d| 50p: %d| 20p: %d| 10p: %d| 5p: %d| 2p: %d| 1p: %d"%(
        x[200]/200, 
        x[100]/100, 
        x[50]/50, 
        x[20]/20, 
        x[10]/10, 
        x[5]/5, 
        x[2]/2, 
        x[1]/1
    )
)