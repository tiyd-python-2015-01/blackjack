
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
        "King", "Ace"]


class Card:
    """Responsibilities:
    Contain a suit and rank.

    Rank - This will be 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King or an
    Ace.

    Suit - There will only be 4 suites. Clubs, Diamonds, Hearts, and Spades.

    Collaborates with:
    Deck
    """

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank


    def __eq__(self, other):
            return self.rank == other.rank and self.suit == other.suit



    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


    def __repr__(self):
        return self.__str__()
