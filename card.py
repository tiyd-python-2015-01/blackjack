"""Card class"""
"""A card will collaborate with Shoe and Hand class"""
"""A card is responsible for knowing its suit and rank"""

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J",
              "Q", "K", "A"]
suits = ["H", "S", "C", "D"]

class Card:
    """Has a rank and a suit. Aces have no value until drawn into a hand"""
    def __init__(self, rank, suit):
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J",
                      "Q", "K", "A"]
        self.suits = ["H", "S", "C", "D"]

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
