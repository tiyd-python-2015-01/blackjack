"""Card class"""
"""A card will collaborate with Deck and Hand class"""
"""A card is responsible for its suit and rank"""

class Card:
    """Has a rank and a suit. Aces have no value until drawn into a hand"""
    def __init__(self, rank, suit):


        self.rank = rank
        self.suit = suit

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return("{} of {}".format(self.rank, self.suit))

    def __repr__(self):
        return self.__str__()
