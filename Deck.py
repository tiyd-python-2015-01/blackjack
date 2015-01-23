"""Deck class"""
"""A Deck collaborates with Card and Shoe"""
"""It is responsible for creating all 52 cards from the Card class
   to be delivered to the Shoe"""
from card import Card, ranks, suits

class Deck:
    """The deck will collect all 52 cards. It will be able to shuffle"""
    def __init__(self):
        self.deck = [Card(rank, suit)
                     for rank in ranks
                     for suit in suits]

    def __str__(self):
        pass
