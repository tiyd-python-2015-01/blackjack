import random
import card


class Deck:
    """A collection of playing cards

    Responsibilities:

    * Maintains a list of available cards to deal
    * Methods:
        - Shuffle()  shuffles the deck
        - Deal() deals a card and updates the deck
        - get_length() tells me how many card I have

    Collaborators:

    * Collects Cards
    * Dealer controls it
    * After a Deal, the Cards go into a Hand
    """
# Creates a single deck

    def __init__(self):
        self.deck = [card.Card(rank, suit)
                     for rank in card.ranks
                     for suit in card.suits]

    def get_length(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        return self

    def deal(self):
        pos = random.randint(0, self.get_length()-1)
        return self.deck.pop(pos)

    def __eq__(self, other):
        return self.deck == other.deck

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "{}".format(self.deck)

    def __str__(self):
        """String representation of a deck."""
        return "{}".format(self.deck)
