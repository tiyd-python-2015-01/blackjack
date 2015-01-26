from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player
from blackjack.dealer import Dealer


class Game:
    """I kinda mucked this up, and rather than having the game run
    through this class, it ended up just basically being a repository
    for miscellaneous functions that were part of the game play"""

    def __init__(self):
        pass

    def create_and_shuffle_deck(self):
        """Creates and shuffles deck"""
        deck = Deck()
        deck.shuffle()
        return deck

    def blackjack_check(self, hand):
        """checks to see if a hand has blackjack.  To be used only
        at a juncture where the hand has only 2 cards."""
        if hand.value == 21:
            return True
        else:
            return False

    def bust_check(self, hand):
        """checks to see whether a hand has busted, ie has value over 21"""
        if hand.value > 21:
            return True
        else:
            return False

    def higher_hand(self, p_hand, d_hand):
        """if both player and dealer stand, checks to see who wins"""
        if p_hand.value == d_hand.value:
            return 'push'
        elif p_hand.value > d_hand.value:
            return 'p_hand'
        else:
            return 'd_hand'
