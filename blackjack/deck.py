import card
import random


class Deck:
    """
    Responsibilities:
    Makes a list of tuples of each card in the deck, of 52 cards.
    It will draw cards randomly for the player, and the dealer.

    Collaborates with:
    Player, Dealer, Shoe, and Cards."""
    def __init__(self):
        self.cards = [card.Card(rank, suit) for rank in card.ranks
                     for suit in card.suits]

    def __str__(self):
        return str(self.cards)

    def deal_card(self):
        new_card = self.cards.pop(random.randint(0,51))
        return new_card
