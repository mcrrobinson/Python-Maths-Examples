import circles

def costOfPizza(diameter, costPerSquareArea):
    """ costOfPizza

    Calculates the cost of the pizza by taking in the
    diameter and using the area of the circle to calculate
    the base by the arbitrary 1.5 given in the task.

    passes:
        diameter:
            Takes in the diameter for used to calculate the
            area of the circle.
    
    returns:
        The cost of the pizza in £.
    """
    circleMath = circles.Circles()
    return circleMath.areaOfcricle(diameter/2) * costPerSquareArea

print(costOfPizza(10, 1.5))