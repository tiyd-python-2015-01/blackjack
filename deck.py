import random
from card import Card

class Deck:
    """A shuffled deck of playing cards.

    Responsibilities:
    *Constructs a deck containing 1 of each card.
    *Has a shuffle method to randomize the order

    collaborators:
    +Collects 1 of each card from the Card class.
    """


    def __init__(self):
        suits = ['♡', '♢', '♧', '♤']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = []
        for rank in ranks:
            for suit in suits:
                card = Card(suit, rank)
                self.cards.append(card)


    def __str__(self):
        deck_list = [str(card) for card in self.cards]
        deck_list = ''.join(deck_list)
        return deck_list
