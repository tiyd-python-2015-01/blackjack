from blackjack import card
import random


class Deck:
    """
    Responsibilities:
    Makes a list of tuples of each card in the deck, of 52 cards.
    It will draw cards randomly for the player, and the dealer.

    Collaborates with:
    Player, Dealer, Shoe, and Cards."""


    def __init__(self):
        self.cards = [card.Card(rank, suit)
                     for rank in card.ranks
                     for suit in card.suits]


    def __str__(self):
        return str(self.cards)


    def __eq__(self, other):
        return self.cards == other.cards


    def deal_card(self):
        new_card = self.cards.pop(random.randint(0, len(self.cards) - 1))
        return new_card


    def __len__(self):
        return len(self.cards)


    def make_shoe(self, number_of_decks):
        return (self.cards * number_of_decks)


class Shoe(Deck):
    def __init__(self, number_of_decks):
        super().__init__()
        self.cards = self.cards * number_of_decks
