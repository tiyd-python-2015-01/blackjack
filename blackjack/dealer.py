from card import Card
from deck import Deck

class Player:
    """The CPU Player playing the game human player

    Responsibilities:

    * Has an active hand of dealt cards
    * Calculates the point value of hand
    * Makes decision on whether to hit or stand

    Collaborators:

    * Recives cards from Deck class.
    * Interacts with Game Class
    * Interacts with Interface Class"""

    def __init__(self, deal_hand=[]):
        self.deal_hand = deal_hand

    def __len__(self):
        """Keeps up with amount of cards in hand"""
        return len(self.deal_hand)

    def __str__(self):
        """String representation of player hand as list of cards."""
        return str([hand for hand in self.deal_hand])

    def __repr__(self):
        return self.__str__()

    def dealer_hit(self, deck):
        card = deck.draw()
        return self.deal_hand.append(card)

    def hand_value(self):
        value = 0
        for card in self.deal_hand:
            value = value + card.value
        return value
