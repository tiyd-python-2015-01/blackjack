"""Deck class"""
"""A Deck collaborates with Card and Shoe"""
"""It is responsible for creating all 52 cards from the Card class
   to be delivered to the Shoe"""
from card import Card

class Deck:
    """The deck will collect all 52 cards. It will be able to shuffle"""
    def __init__(self):


        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J",
                      "Q", "K", "A"]
        self.suits = ["H", "S", "C", "D"]
        self.deck = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
