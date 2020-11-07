from logging import basicConfig, error, info, INFO
from sys import argv

class WeightConverter(object):
    """
    docstring
    """
    def __init__(self, user_weight):
        self.user_weight = user_weight

    def ToKg(self):
        return self.user_weight * 0.45359237

    def ToLbs(self):
        return self.user_weight / 0.45359237

def main():
    """
    docstring
    """
    try:
        user_input = int(argv[1])
    except IndexError:
        error("Please input a number, you entered nothing.")
        exit(1)

    except ValueError:
        error("Please input a valid number, not a string.")
        exit(1)

    info("Input to KG: %f", WeightConverter(user_input).ToKg())
    info("Input to LBS: %f", WeightConverter(user_input).ToLbs())

if __name__ == "__main__":
    basicConfig(level=INFO, format='%(asctime)s | %(levelname)s | %(message)s')
    main()