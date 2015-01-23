from deck import *
from hand import *

class Dealer:
    """A dealer for the game.

    Responsibilities:

        * Has a hand of cards
        * Has a budget
        * Has a status: Bust, Hit, Stand
        * Methods:
            Gets_budget()
            Gets_status()

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

    def add_card(self,card):
        self.__hand__.add_card(card)


    def updates_status(self, newstatus):
        self.__status__ = newstatus

    def get_status(self):
        return self.__status__

    def __repr__(self):
        return "{}".format(self.__name__)

    def __str__(self):
        return "{}".format(self.__name__)
