
class Card:

    def __init__(self, number, suit, value):

        self.value = value
        self.suit = suit
        self.number = number

    def __str__(self):
        return "{} of {}".format(self.number, self.suit)

    def __repr__(self):
        return self.__str__()
