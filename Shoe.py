"""Shoe class"""
"""Shoe collaborates with Deck and Hand"""
"""It is responsible for receiving decks from Deck, shuffling the decks,
   and dealing to the Hand"""
from deck import Deck as dk
import random

class Shoe:
    """Collects decks. Shuffles. Deals cards to hands"""
    def __init__(self, decks=1):

        self.shuffle_shoe = random.shuffle(dk.deck)
        print(shuffle_shoe)


    # def __str__(self):
