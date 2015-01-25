
suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card:
    """A playing card.

    Responsibilities:

    * Has a rank and a suit.
    * Has a point value. Aces point values depend on the Hand.
    * Methods:
        get_value() to get the value of a card
        get_rank() returns the card rank
        get_suit() returns the card suit

    Collaborators:

    * Collected into a Deck.
    * Collected into a Hand for player and a Hand for the dealer.
    """


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        if self.rank == "A":
            return 1
        elif self.rank in ["J", "Q", "K"]:
            return 10
        else:
            return int(self.rank)

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def __repr__(self):
        return "'{} of {}'".format(self.rank, self.suit)

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
