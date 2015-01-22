from card import Card
from random import shuffle


#assign unicode chararcters for each suit
Clubs, Diamonds, Hearts, Spades = u'\u2663', u'\u2666', u'\u2665', u'\u2660'
SUITS = (Clubs, Diamonds, Hearts, Spades)
RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A')


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
        self.__cards__ = [Card(rank, suit)
                      for rank in RANKS
                      for suit in SUITS]


    def draw(self):
        """Take a card off the top of the deck and return it"""
        return self.__cards__.pop()


    def shuffle(self):
        """Shuffles cards in the deck"""
        shuffle(self.__cards__)
        return self.__cards__


    def __eq__(self, other):
        return self.__cards__ == other.__cards__

    def __len__(self):
        return len(self.__cards__)

    def __str__(self):
        deck_list = [str(card) for card in self.__cards__]
        return ", ".join(deck_list)

    def __repr__(self):
        return self.__str__()
