import random

from card import Card
from deck import Deck


class Shoe:
    """ A collection of 1-6 decks.

    Responsibilities:
    *take an argument for the number of decks
    *combine and shuffle decks
    *pop the last item off of the shuffled deck and send it to either
     player_hand or dealer_hand

    Collaborators:
    *gets decks to combine into shoe
    * pops the last item off of the shuffled deck and send it to either
    the dealer's Hand or the player's Hand"""

    def __init__(self, an_int, a_deck):
        self.decks = an_int
        self.shuffle = random.shuffle(a_deck.cards * an_int)


    def __str__(self):
        card_list = [str(card) for card in self.shuffle]
        return ', '.join(card_list)


    def __repr__(self):
        return self.__str__

a_shoe = Shoe(1)
print(a_shoe)
