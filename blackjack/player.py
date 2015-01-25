from hand import *


class Player:
    """A player.

    Responsibilities:

    * Has a hand of cards
    * Has a budget
    * Has a status: Bust, Hit, Stand
    * Methods:
        Gets_budget()
        Updates_budget()
        Gets_status() "H for Hit, S for stand, B for bust"
        Updates_status()

    Collaborators:

    * Has a hand of cards
    * Receives cards from the deck
    * Methods:
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
    Get_budget
    Set_budget

    """

    def __init__(self, name, budget):
        self.__name__ = name
        self.__status__ = ''
        self.__budget__ = budget
        self.__hand__ = Hand()

    def get_name(self):
        return self.__name__

    def add_card(self, card):
        self.__hand__.add_card(card)

    def get_hand_value(self):
        return self.__hand__.get_value()

    def get_hand_status(self):
        return self.__hand__.get_hand_status()

    def set_hand_status(self, status):
        return self.__hand__.set_hand_status(status)

    def set_budget(self, change):
        self.__budget__ += change

    def get_budget(self):
        return self.__budget__

    def set_status(self, newstatus):
        self.__status__ = newstatus

    def get_status(self):
        return self.__status__

    def get_hand(self):
        return self.__hand__

    def __repr__(self):
        return "{}".format(self.__name__)

    def __str__(self):
        return "{}".format(self.__name__)
