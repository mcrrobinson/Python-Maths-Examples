def travelStatistics(averageSpeed, duration, kmPerLitre):
    """ travelStatistics

    Converts the distance and duration of a car journey
    to the amount of fuel used in liters assuming a 
    fuel efficiency of 5km/litre.

    passes:
        averageSpeed:
            Takes in average speed in kilometers per hour.
        duration:
            Takes in duration in hours.

    returns:
        distranceTravelled:
            Returns the distance travelled in kilometers.
        fuelUsage:
            Returns the fuel usage in liters.
    """
    distranceTravelled = averageSpeed * duration
    fuelUsage = distranceTravelled/kmPerLitre
    return distranceTravelled, fuelUsage

print(travelStatistics(50, 60, 5))