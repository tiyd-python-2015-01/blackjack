from random import shuffle
from blackjack.card import Card, ranks, suits


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

        self.cards = [Card(rank, suit) for suit in suits
                      for rank in ranks
                      for deck in range(self.decks)]
        shuffle(self.cards)

    def __len__(self):
        return len(self.cards)
        
    def deal(self):
        """Pops a single card from the end of the card list and returns
        it to the calling function"""
        return self.cards.pop()
