suits = ("Spades", "Clubs", "Hearts", "Diamonds")
ranks = ("Ace", "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2,)


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

    def __eq__(self, other):
        """test equality for two cards."""
        return self.suit == other.suit and self.rank == other.rank

    def __repr__(self):
        return "Card(rank = {}, suit = {})".format(self.rank, self.suit)
