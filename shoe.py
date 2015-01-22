from deck import Deck
from random import shuffle


class Shoe:
    """A multi-deck dealer.

    Responsibilities:

    * Holds x number of Decks.


    Collaborators:

    * Holds Decks.
    * Deals Cards to player and dealer's hands.
    """
    pass
    # def __init__(self, number_of_decks):
    #     self.number_of_decks = number_of_decks
    #     self.cards = [Card() for _ in range(number_of_decks) * 52]
    #
    # def shuffle(self):
    #     shuffle(self.cards)
    #
    # def __str__(self):
    #     shoe_list = [str(card) for card in self.cards]
    #     return ", ".join(shoe_list)
    #
    # def __repr__(self):
    #     return self.__str__()
