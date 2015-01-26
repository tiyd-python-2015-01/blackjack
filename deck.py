import card
import random


class Deck:
    """Assembles a deck of 52 cards, collaborates with Cards"""

    def __init__(self):
        """Makes 52 cards"""
        self.deck = [card.Card(number, suit) for suit in card.card_suits for
                     number in card.card_numbers]

    def __len__(self):
        """allows the len fn to be used on Deck class"""
        return len(self.deck)

    def __str__(self):
        """Shows the deck when printing"""
        return str(self.deck)

    def get_card(self):
        """Pulls one random card from the deck"""
        return self.deck.pop(random.randint(0, len(self.deck)-1))

    def refill(self):
        """refills the deck to 52 cards"""
        self.deck = [card.Card(number, suit) for suit in card.card_suits for
                     number in card.card_numbers]
