"""
Shoe
    Responsibilities:
        -Generate Deck(s)   -Shuffles Deck(s)   -Gives Card(s)
    Collaborators
        -Deck   -Card   -Game_State     -Table_State
        -Player     -Human_Player   -Dealer

Deck
    Responsibilities:
        -Generate Card Variations
    Collaborators
        -Card   -Shoe
Card
    Responsibilities:
        -Name   -Suit   -Value?
    Collaborators
        -Hand   -Deck   -Table_State    -Shoe   -Player
"""
from random import shuffle, randint

SUITS = ['♧', '♢', '♤', '♡']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'King', 'Queen', 'Joker', 'Ace']


class Shoe:
    """Shoe handles most of the work of these classes.
    Shoe initializes itself as a list of decks but then uses self.cards
    as the single list of all the cards being played in the game.  """
    
    def __init__(self, number_of_decks=1):
        self.decks = [Deck() for n in range(number_of_decks)]
        self.cards = [card for deck in self.decks for card in deck.cards]

    def shuffle(self):
        shuffle(self.cards)

    def deal_hand(self):
        hand = [self.cards.pop(), self.cards.pop()]
        return hand

    def give_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return 0

    def __str__(self):
        return str(self.cards)


class Deck:
    """Deck contains a list of unique cards.
    Give_card() pops one card off the list """
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def give_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return 0

    def __str__(self):
        return str(self.cards)


class Card:
    """ Simple Card class contains two attributes (rank and suit)
    Representation, String and Equality are all defined and used by other
    containing classes"""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __repr__(self):
        return self.__str__()

    def __eq__(self,other_card):
        if self.rank == other_card.rank and self.suit == other_card.suit:
            return True
        else:
            return False
