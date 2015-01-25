from deck import *
from hand import *


class Dealer:
    """A dealer for the game.

    Responsibilities:

        * Has a hand of cards
        * Has a budget
        * Has a status: Bust, Hit, Stand
        * Methods:
            Deal() - gives one card
            add_card() adds a card to its hand
            Get_hand()) returns the cards in the hand
            get_hand_value() returns the value of the hand
            get_hand_status() the hand status is hard or soft
                (1 A with value of 11)
            set_hand_status() changes the value of the hand from
                hard to soft and viceversa
            Get_status() Status is Hit when dealer still getting cards.
                Bust when dealer goes over 21
            Set_status: sets to B when dealer busts, set to T when there is
                a tie (push)
        Collaborators:

        * Has a hand of cards
        * Receives cards from the deck
        * Controls the deck
        """

    def __init__(self):
        self.__deck__ = Deck().shuffle()
        self.__status__ = ''
        self.__hand__ = Hand()

    def deal(self):
        return self.__deck__.deal()

    def add_card(self, card):
        self.__hand__.add_card(card)

    def get_hand(self):
        return self.__hand__

    def get_hand_value(self):
        return self.__hand__.get_value()

    def get_hand_status(self):
        return self.__hand__.get_hand_status()

    def set_hand_status(self, status):
        return self.__hand__.set_hand_status(status)

    def set_status(self, newstatus):
        self.__status__ = newstatus

    def get_status(self):
        return self.__status__

    def __repr__(self):
        return "{}".format(self.__name__)

    def __str__(self):
        return "{}".format(self.__name__)
