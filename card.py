class Card:
    """Playing card.

    Responsibilities:

    *Card has a rank and a suit.

    Collaborators:

    *Collected in a Deck
    *Collected in a Hand for the players and a Hand for the dealer.
    """


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def __str__(self):
        return'{}{}'.format(self.rank, self.suit)
