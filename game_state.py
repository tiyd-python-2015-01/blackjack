import random
from hand import Hand
from shoe import Shoe


class Game():
    """Contains the initial state of a game, as well as methods for actions and
    results within the game.

    Responsiblities:
    *Initiates new hands for the player and dealer
    *Contains the hit method for drawing cards into those hands

    Collaborators:
    +Collects hands from Hand
    +Collects the Shoe
    """
    def __init__(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.shoe = Shoe()

    def __str__(self):
        return ' '.join([cards.__str__() for cards in self.player.hand])

    def deal(self):
        """Method for the initial card dealing to the player and dealer."""
        for _ in range(2):
            self.player_hand.cards.append(self.shoe.draw())
        for _ in range(2):
            self.dealer_hand.cards.append(self.shoe.draw())

    def hit(self):
        """Allows the player draw another card (hit)."""
        self.player_hand.cards.append(self.shoe.draw())

    def dealer_hit(self):
        """Allows the dealer draw another card (hit)."""
        self.dealer_hand.cards.append(self.shoe.draw())
