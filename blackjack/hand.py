from card import *


class Hand:
    """A collection of cards for a dealer or a player

    Responsibilities:

    * Holds cards
    * Holds status: soft or hard

    Collaborators:

    * Cards
    * Player
    * Dealer
    * add_card()
    * get value()
    * get_status(): soft or hard  "soft has a card valued as 11"
    """

# Creates hand

    def __init__(self):
        self.__cards__ = []
        self.__status__ = 'H'

    def update_hand_status(self, newstatus):
        self.__status__ = newstatus

    def get_hand_status(self):
        return self.__status__

    def add_card(self, card):
        self.__cards__.append(card)
        return self

    def get_value(self):
        total = 0
        for i in range(0,len(self.__cards__)):
            total += self.__cards__[i].get_value()
        if self.__status__ == "S":
            total += 10
        return total

    def __len__(self):
        return len(self.__cards__)

    def __repr__(self):
        return "{}".format(self.__cards__)

    def __str__(self):
        return "{}".format(self.__cards__)
