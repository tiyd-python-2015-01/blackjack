import random

from blackjack.card import Card


class Deck:
    """A set of 52 playing cards.

    Responsibilities:
    * hold a collection of cards
    * self-generates a list of 52 cards of every variation
    * Should be able to (re)shuffle itself
    * should be able to report its current size

    Collaborators:
    * consists of cards"""

    def __init__(self):
        ranks = ['2',
                 '3',
                 '4',
                 '5',
                 '6',
                 '7',
                 '8',
                 '9',
                 '10',
                 'J',
                 'Q',
                 'K',
                 'A']
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        return random.shuffle(self.cards)

    def __str__(self):
        card_list = [str(card) for card in self.cards]
        return ', '.join(card_list)

    def __repr__(self):
        return self.__str__()
