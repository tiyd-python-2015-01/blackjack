"""Hand class"""
"""Hand collaborates with Shoe and the Player"""
"""Hand receives cards from Shoe, calculates a value for Player"""

from card import Card, ranks, suits
from shoe import Shoe


class Hand:
    """Hand will know which cards it has, the value of those cards.
       It will receive two cards to start, then more depending on player
       action."""

    def __init__(self):
        """Creates instance of Hand"""
        self.hand = []

        self.values = {"1" : 1, "2" : 2,"3" : 3, "4" : 4, "5" : 5, "6" : 6,
                       "7" : 7, "8" : 8, "9": 9, "10" : 10, "J" : 10, "Q" : 10,
                       "K" : 10, "A" : 11}


    def add_card(self, card):
        """Adds a card from the shoe to the hand"""
        self.hand.append(card)
        return self.hand


    def get_hand_value(self, shoe):
        """Determines the value of a hand based on the cards therein."""
        card = shoe.deal_card()
        rank = card.get_rank(card)
        self.hand_value = 0
        current_hand_value =+ self.values[rank]
        if self.hand.count("A") in self.hand > 1:
            current_hand_value = 12
        elif current_hand_value > 21 and "A" in Hand:
            current_hand_value -= 10
        else:
            current_hand_value
        return current_hand_value
