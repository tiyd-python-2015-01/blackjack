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

        self.values = {"2" : 2,"3" : 3, "4" : 4, "5" : 5, "6" : 6,
                       "7" : 7, "8" : 8, "9": 9, "10" : 10, "J" : 10, "Q" : 10,
                       "K" : 10, "A" : 1}


    def add_card(self, card):
        """Adds a card from the shoe to the hand"""
        player_hand = self.hand.append(card)
        return player_hand


    def get_hand_value(self, shoe):
        """Determines the value of a hand based on the cards therein."""
        card = shoe.deal_card()
        rank = card.get_rank(card)
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += self.values[rank]
            if rank == "A":
                ace_in_hand = True
        if not ace_in_hand:
            return self.hand_value
        else:
            if self.hand_value + 10 <= 21:
                self.hand_value + 10
                return self.hand_value
            else:
                return self.hand_value
