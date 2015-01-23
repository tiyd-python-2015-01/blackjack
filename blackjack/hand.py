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

# Creates hand with 2 initial cards

    def __init__(self, card1, card2):
        self.__cards__ = [card1, card2]
        self.__status__ = 'H'

    def update_hand_status(self, newstatus):
        self.__status__ = newstatus

    def get_hand_status(self):
        return self.__status__

    def add_card(self, card):
        self.__cards__.append(card)
        return self.__cards__

    def __len__(self):
        return len(self.__cards__)

    def __repr__(self):
        return "{}".format(self.__hand__)

    def __str__(self):
        return "{}".format(self.__hand__)
