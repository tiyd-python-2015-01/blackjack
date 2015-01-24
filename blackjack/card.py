
class Card:
    """A playing card.

    Responsibilities:

    * Has a rank and a suit.
    * Has a point value. Aces point values depend on the Hand.

    Collaborators:

    * Collected into a Deck.
    * Collected into a Hand for each player and a Hand for the dealer.
    """

    def __init__(self, rank, suit): ###This is a constructor
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
    ###does value need to be determined somewhere else instead?

    def swap_ace(self):
        if self.value == 11:
            self.value = 1
        else:
            self.value = 11

    def __eq__(self,other_card):
        if self.rank == other_card.rank and self.suit == other_card.suit:
            return True
        else:
            return False

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __repr__(self):
        return self.__str__()
