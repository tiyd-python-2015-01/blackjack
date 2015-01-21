from card import Card


SUITS = ('Spade', 'Hearts', 'Diamonds', 'Clubs')
RANKS = (2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace')

class Deck:
    """A playing card deck.

    Responsibilities:

    * Can hold cards.

    Collaborators:

    * Can hold cards.
    * Can be put into shoe for dealing and shuffling
    """
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        self.max_cards = 52

    def __str__(self):
        deck_list = [str(card) for card in self.cards]
        return ", ".join(deck_list)

    def __repr__(self):
        return self.__str__()
