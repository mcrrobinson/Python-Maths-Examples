import math

class Circles:

    def circumferenceOfCircle(self, radius):
        """ circumferenceOfCircle

        Uses the radius to return the circumference of a circle.

        passes:
            radius:
                Passes in the radius of the circle to be
                circumference calculated.
        
        returns:
            The circurference of the circle.
        """
        return 2 * math.pi * radius

    def areaOfcricle(self, radius):
        """ areaOfcricle

        Works out the area of a circle by using the radius.

        passes:
            radius:
                Passes in the radius to calculate the area of
                the circle.
        
        returns:
            Returns the cm sqaured of a circle area.
        """
        return math.pi * radius**2

if __name__ == "__main__":
    CircleMath = Circles()
    radius = 5 

    print(CircleMath.circumferenceOfCircle(radius))
    print(CircleMath.areaOfcricle(radius))