from logging import basicConfig, error, info, INFO
from sys import argv
import argparse

class WeightConverter(object):
    """ WeightConverter

    Converts between pounds and kilograms.

    Passes:
        user_weight:
            This can be in either pounds or kilograms depending
            on the users flag of choice.
    Returns:
        user_Weigt: 
            Returns the entered weight to the chosen measuring
            standard.
    """
    def __init__(self, user_weight):
        self.user_weight = user_weight

    def ToKg(self):
        return self.user_weight * 0.45359237

    def ToLbs(self):
        return self.user_weight / 0.45359237

def main(parser):
    parser.add_argument('-kg_to_lb', action="store")
    parser.add_argument('-lb_to_kg', action="store")
    args = parser.parse_args()

    if args.lb_to_kg:
        info("Input to KG: %f", WeightConverter(int(args.lb_to_kg)).ToKg())
    elif args.kg_to_lb:
        info("Input to LBS: %f", WeightConverter(int(args.kg_to_lb)).ToLbs())
    else:
        error("Enter one the flags followed by the argument; -kg_to_lb or lb_to_kg. \nE.g. (python main.py -kg_to_lb 83)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Converts between pounds and kilograms.',
    )
    basicConfig(level=INFO, format='%(asctime)s | %(levelname)s | %(message)s')
    main(parser)
