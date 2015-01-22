class Card:
    """A playing card.

    Responsibilities:

    * Has a rank and suit

    Collaborators:

    * Collected into a Deck
    * Collected into a Hand for each player and a Hand for the dealer.
    """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __repr__(self):
        return self.__str__
