"""Shoe class"""
"""Shoe collaborates with Deck and Hand"""
"""It is responsible for receiving decks from Deck, shuffling the decks,
   and dealing to the Hand"""
from deck import Deck
from card import Card, ranks, suits
import random


class Shoe:
    """Collects decks. Shuffles. Deals cards to hands"""
    def __init__(self, decks=1):

        self.deck = [Card(rank, suit)
                     for rank in ranks
                     for suit in suits]


    def __str__(self):
        pass


    def shuffle_shoe(self):
        """Shuffles the deck"""
        random.shuffle(self.deck)
        return self.deck

    def deal_card(self):
        """Deals a card"""
        dealt_card = self.deck.pop()
        return dealt_card
