"""Card class"""
"""A card will collaborate with Deck and Hand class"""
"""A card is responsible for its suit and rank"""

class Card:
    """Has a rank and a suit. Aces have no value until drawn into a hand"""
    def __init__(self, suit, rank):


        self.rank = rank
        self.suit = suit

    def get_suit():
        return self.suit

    def get_rank():
        return self.rank
