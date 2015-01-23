"""Hand class"""
"""Hand collaborates with Shoe and the Player"""
"""Hand receives cards from Shoe, calculates a value for Player"""

from card import Card, ranks, suits
from deck import Deck

class Hand:
    """Hand will know which cards it has, the value of those cards.
       It will receive two cards to start, then more depending on player
       action."""

    def __init__(self, *Card):

        self.rank = get_rank(Card)
        self.values = {"1" : 1, "2" : 2,"3" : 3, "4" : 4, "5" : 5, "6" : 6,
                  "7" : 7, "8" : 8, "9": 9, "10" : 10, "J" : 10, "Q" : 10,
                  "K" : 10, "A" : 11}

        hand_value = sum(self.value(Card))
        self.hand = []

    def add_card(self, Card):
        self.hand.append(Card)

    def get_hand_value(self):
        current_hand_value = [card_value for value in self.values()]
        if list.count("A") in self.hand > 1:
            current_hand_value = 12
        elif current_hand_value > 21 and "A" in Hand:
            current_hand_value -= 10
        else:
            current_hand_value
        return current_hand_value
