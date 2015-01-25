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
        self.cards = [card.Card(rank, suit)
                     for rank in card.ranks
                     for suit in card.suits]


    def __str__(self):
        return str(self.cards)


    def __eq__(self, other):
        return self.cards == other.cards


    def shuffle(self):
        """Lets the deck shuffle when down to 26 cards."""
        random.shuffle(self.cards)


    def deal_card(self):
        """Returns a new, random card, from within the deck. Checks to see
        if the deck has only 26 cards. If it does the deck is shuffled."""
        new_card = self.cards.pop(random.randint(0, len(self.cards) - 1))
        if len(self.cards) == 26:
            self.cards.shuffle()
        return new_card


    def __len__(self):
        return len(self.cards)


class Shoe(Deck):
    def __init__(self, number_of_decks):
        super().__init__()
        self.cards = self.cards * number_of_decks
