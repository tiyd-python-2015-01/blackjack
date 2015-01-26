
card_suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
card_numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace",
                "King", "Queen", "Jack"]


class Card:
    """The basic card, stores only a rank (number) and a suit"""

    def __init__(self, number, suit):

        self.suit = suit
        self.number = number

    def __str__(self):
        return "{} of {}".format(self.number, self.suit)

    def __repr__(self):
        return self.__str__()
