from card import Card
from deck import Deck
from random import shuffle


class Dealer_Hand:
    """Creates a dealer hand.

    Responsiblities:
    * Creates a dealer hand by drawing card from the deck.
    * Determine the value of given cards in hand.
    * Show one card and leave the other card a secret.

    Collaborators:
    * Deck
    """

    def __init__(self, hand=None):
        if hand is None:
            hand = []
        self.hand = hand

    def __str__(self):
        """Player hand is represented by string of cards"""
        return str([hand for hand in self.hand])

    def draw_two(self, deck):
        self.hand = []
        card1 = deck.draw()
        card2 = deck.draw()
        self.hand.append(card1)
        self.hand.append(card2)
        return self.hand

    def hit(self, card):
        return self.hand.append(card)

    def hand_value(self):
        value = 0
        for card in self.hand:
            value = value + card.value
        return value
