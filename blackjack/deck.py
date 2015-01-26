from random import shuffle
from card import Card

class Deck:
    """A single deck of 52 playing card.

    Responsibilities:
    * Hold a colleciton of cards.
    * Have one of every card present
    * Be able to shuttle itself
    * Deals a Card object from Should all others to draw cards
    * Should be able to report its current size

    Collaborators:

    * Collects the Class Card
    * Get passed into Shoe to keep up with count (hard mode)
    """

    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    ranks = (2,3,4,5,6,7,8,9,10,"Jack", "Queen", "King", "Ace")


    def __init__(self):
        self.deck = [Card(rank, suit) for suit in self.suits
                                      for rank in self.ranks]


    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_card(self):
        """Removes a card from top of deck and make it available to player or
        Dealer"""
        return self.deck.pop(0)

    def __len__(self):
        """Keeps up with amount of cards in deck"""
        return len(self.deck)

    def __str__(self):
        """String representation of a deck as a list of cards."""
        return str(self.deck)


    def __repr__(self):
        return self.__str__()
