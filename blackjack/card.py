class Card:
    """A playing card.

    Responsibilities:

    * Has a rank and a suit.
    * Has a point value. Aces point values depend on the Hand.

    Collaborators:

    * Collected into a Deck.
    * Collected into a Hand for each player and a Hand for the dealer.
    """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.point_value(self.rank)

    def point_value(self, rank):
        if type(rank) == int:
            value = rank
            return value
        elif rank == "Ace":
            value = 11
            return value
        else:
            value = 10
            return value

    def swap_ace(self):
        if self.value == 11:
            self.value = 1
        else:
            self.value = 11

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __repr__(self):
        return self.__str__()
