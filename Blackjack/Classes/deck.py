from random import shuffle
from card import Card

class Deck:
    """A single deck of 52 playing card.

    Responsibilities:

    * Have one of every card present
    * Be shuffled in a random order

    Collaborators:

    * Collects the Class Card
    * Get passed into Deck Counter to keep up with count
    """


    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    ranks = (2,3,4,5,6,7,8,9,10,"Jack", "Queen", "King", "Ace")

    def __init__(self):
        self.deck = [Card(rank, suit) for suit in self.suits
                                     for rank in self.ranks]

    def shuffle_deck(self, deck):
        random.shuffle(deck)

    def __str__(self):
        """String representation of a point."""
        return "Shuffled deck is {})".format(self.shuffleself.x, self.y)


    def __repr__(self):
        return [cards for card in self.deck]
