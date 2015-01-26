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

        self.valuedict = {"2" : 2,"3" : 3, "4" : 4, "5" : 5, "6" : 6,
                       "7" : 7, "8" : 8, "9": 9, "10" : 10, "J" : 10, "Q" : 10,
                       "K" : 10, "A" : 1}


    def __str__(self):
        return "Hand contains {}".format(self.hand)


    def __len__(self):
        return len(self)


    def add_card(self, card):
        """Adds a card from the shoe to the hand"""
        self.hand.append(card)
        return self.hand


    def get_card_value(self, card):
        for card in self.hand:
            card_value = self.valuedict[card.get_rank()]
            return card_value


    def get_hand_value(self):
        has_ace = False
        hand_value = 0
        for card in self.hand:
            card_value = self.valuedict[card.get_rank()]
            hand_value += card_value
        print(hand_value)
        return hand_value
