from card import Card
from random import shuffle


class Deck:
    """Create a Deck of 52 Cards

    Responsiblities:

    * Creates a Deck of Cards
    * Has one of every card present
    * Shuffles Cards in random order

    Collaborators:

    * Collects the Class: Card
    * Gets passed through the Deck Tracker
    """

    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")

    def __init__(self):
        self.deck = [Card(rank, suit) for suit in self.suits
                                      for rank in self.ranks]

    def shuffle_deck(self, deck):
        random.shuffle(deck)

    def __repr__(self):
        return [cards for card in self.deck]
