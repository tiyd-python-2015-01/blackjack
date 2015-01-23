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
