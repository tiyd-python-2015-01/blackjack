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
    """

    def __init__(self, name, budget):
        self.__name__ = name
        self.__status__ = ''
        self.__budget__ = budget
        self.__hand__ = Hand()

    def add_card(self,card):
        self.__hand__.add_card(card)

    def updates_budget(self, change):
        self.__budget__ += change

    def get_budget(self):
        return self.__budget__

    def updates_status(self, newstatus):
        self.__status__ = newstatus

    def get_status(self):
        return self.__status__

    def __repr__(self):
        return "{}".format(self.__name__)

    def __str__(self):
        return "{}".format(self.__name__)
