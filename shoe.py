from deck import Deck
import random


class Shoe:
    """Creates a shoe of 6 decks, collaborates with Deck class"""

    def __init__(self):
        """Fills the shoe with 6 decks"""
        deck = Deck()
        self.shoe = []
        for _ in range(1, 7):
            self.shoe.extend(deck.deck)

    def __len__(self):
        """Allows the len fn to be used on Shoe class"""
        return len(self.shoe)

    def __str__(self):
        """Displays the deck when print is called on Shoe class"""
        return str(self.shoe)

    def get_card(self):
        """Takes one random card out of the Shoe"""
        return self.shoe.pop(random.randint(0, len(self.shoe)-1))

    def refill(self):
        """Refills the shoe with six decks"""
        deck = Deck()
        self.shoe = []
        for _ in range(1, 7):
            self.shoe.extend(deck.deck)
