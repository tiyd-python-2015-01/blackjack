from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player
from blackjack.dealer import Dealer


class Game:

    def __init__(self):
        pass

    def create_and_shuffle_deck(self):
        deck = Deck()
        deck.shuffle()
        return deck

    def blackjack_check(self, hand):
        pass

    def bust_check(self, hand):
        if hand.value > 21:
            return 'bust'
        else:
            return 'ok'

    def higher_hand(self, p_hand, d_hand):
        """if both player and dealer stand, checks to see who wins"""
        if p_hand.value == d_hand.value:
            return 'push'
        elif p_hand.value > d_hand.value:
            return 'p_hand'
        else:
            return 'd_hand'
