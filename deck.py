from card import Card
from random import shuffle


#assign unicode chararcters for each suit
Clubs, Diamonds, Hearts, Spades = u'\u2663', u'\u2666', u'\u2665', u'\u2660'
SUITS = (Clubs, Diamonds, Hearts, Spades)
RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')


class Deck:
    """A playing card deck.

    Responsibilities:

    * Can hold cards.
    * New deck should have all 52 cards.
    * Should allow others to draw cards.
    * Should be able to reshuffle itself
    * Should be able to report its current size

    Collaborators:

    * Can hold cards.
    * Can be put into shoe for dealing and shuffling
    """
    def __init__(self):
        self._cards = [Card(rank, suit)
                      for rank in RANKS
                      for suit in SUITS
                      ]


    def draw(self):
        """Take a card off the top of the deck and return it"""
        return self._cards.pop()


    def shuffle(self):
        """Shuffles cards in the deck"""
        shuffle(self._cards)
        return self


    def __eq__(self, other):
        return self._cards == other._cards

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        deck_list = [str(card) for card in self._cards]
        return ", ".join(deck_list)

    def __repr__(self):
        return self.__str__()
