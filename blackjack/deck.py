from random import shuffle
from card import Card


class Deck:
    """Deck of cards class.  A deck of cards is a collection of card objects.

    Responsibilities:

    * The Deck class generates a series of Card objects corresponding with
      the required cards in a complete deck of cards.
    * It is also responsible for randomizing the location of the cards
      within the deck list.
    * Takes an optional argument decks at creation to allow for creation of
      a shoe containing any number of decks.

    Collaborators:

    * Deck collects Card Objects
    * Deck pops and returns cards from it's card list when requested by
      a calling function.
    * Deck can be reinitialized by an outside function by calling the
      reshuffle method.
    """

    def __init__(self, decks=1):
        self.decks = decks
        suits = ["hearts", "spades", "clubs", "diamonds"]
        names = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                 "10", "J", "Q", "K"]
        self.cards = [Card(name, suit) for suit in suits
                      for name in names
                      for deck in range(self.decks)]
        shuffle(self.cards)

    def deal(self):
        """Pops a single card from the end of the card list and returns
        it to the calling function"""
        return self.cards.pop()

    def reshuffle(self):
        """Reinitializes the deck"""
        self.__init__()
