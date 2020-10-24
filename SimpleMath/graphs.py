import math

class Graphs:

    def slopeOfLine(self,x1,y1,x2,y2):
        """ slopeOfLine

        Calculates the gradient of a slope from x1,y1 to x2,y2

        passes:
            x1:
                Takes in the point in order to calculate the
                slope curve.
            y1:
                Takes in the point in order to calculate the
                slope curve.
            x2:
                Takes in the point in order to calculate the
                slope curve.
            y2:
                Takes in the point in order to calculate the
                slope curve.
        
        returns:
            Returns the gradient of the curve.
        """
        return (y2-y1)/(x2-x1)

    def distanceBetweenPoints(self,x1,y1,x2,y2):
        """ distanceBetweenPoints

        Calculates the distance between the point using
        pythagoruses theorum.

        passes:
            x1:
                Takes in the point in order to calculate the distance
                between the x1,y1 to x2,y2.
            y1:
                Takes in the point in order to calculate the distance
                between the x1,y1 to x2,y2.
            x2:
                Takes in the point in order to calculate the distance
                between the x1,y1 to x2,y2.
            y2:
                Takes in the point in order to calculate the distance
                between the x1,y1 to x2,y2.
        
        returns:
            Returns the distance between x1,y1 and x2,y2.
        """
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

if __name__ == "__main__":
    Graphs = Graphs()
    print(Graphs.slopeOfLine(2,4,6,8))
    print(Graphs.distanceBetweenPoints(2,4,6,8))