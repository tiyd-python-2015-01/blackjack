from blackjack.card import Card, ranks, suits
import random


class Deck:
    """A deck of cards.

    Responsibilities:

    * Has a collection of cards
    * Should be able to (re)shuffle itself
    * Should allow others to draw cards
    * New deck should have all 52 cards
    * Be able to report its current size

    Collaborators:

    * Collected from card class.
    * Deals cards to Dealer_hand and Player_hand class """

    def __init__(self):
        self.card_deck = [Card(rank, suit)
                          for rank in ranks
                          for suit in suits]

    def __str__(self):
        return str(self.card_deck)

    def __len__(self):
        return len(self.card_deck)

    def shuffle_deck(self):
        """shuffles the card deck"""

        random.shuffle(self.card_deck)
        return self.card_deck

    def card_count(self):
        """ Counts how many cards are in the deck"""

        count = len(self)
        return count

    def deal_card(self):
        """Pulls a card out of the deck and returns its value"""
        return self.card_deck.pop()
