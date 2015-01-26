from collections import namedtuple


"""A playing card.

Responsibilities:

* Has a rank and suit

Collaborators:

* Collected into a Deck
* Collected into a Hand for each player and a Hand for the dealer.
"""


class Card(namedtuple('card', ['rank', 'suit'])):

    __memory__ = ()  # assure instance is stored as a tuple in memory

    def __str__(self):
        return "{}{}".format(self.rank, self.suit)

    def __repr__(self):
        return self.__str__()
