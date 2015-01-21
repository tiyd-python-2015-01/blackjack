"""Hand class"""
"""Hand collaborates with Shoe and the Player"""
"""Hand receives cards from Shoe, calculates a value for Player"""


class Hand:
    """Hand will know which cards it has, the value of those cards.
       It will receive two cards to start, then more depending on player
       action."""

    def __init__(self, Card):

        self.value = get_rank(Card)
        values = {"1" : 1, "2" : 2,"3" : 3, "4" : 4, "5" : 5, "6" : 6,
                  "7" : 7, "8" : 8, "9": 9, "10" : 10, "J" : 10, "Q" : 10,
                  "K" : 10, "A" : 1]

        hand_value = sum(self.value(Card))
