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

SUITS = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
FACES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'King', 'Queen', 'Joker', 'Ace']


class Shoe:
    def __init__(self, number_of_decks=1):
        self.decks = [Deck() for n in range(number_of_decks)]
        self.cards = [card for deck in self.decks for card in deck.cards]

    def shuffle_shoe(self):
        shuffle(self.cards)


class Deck:
    def __init__(self):
        self.cards = [Card(face, suit) for suit in SUITS for face in FACES]

    def get_card(self):
        return self.cards.pop()


class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.face, self.suit)

    def __repr__(self):
        return self.__str__()
