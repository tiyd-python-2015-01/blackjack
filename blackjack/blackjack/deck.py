from card import Card

class Deck:
    """A set of 52 playing cards.

    Responsibilities:
    * self-generates a list of 52 cards of every variation

    Collaborators:
    * consists of cards
    * collected into a Shoe, either by itself or with multiple decks"""


    def __init__(self):
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]


    def __str__(self):
        card_list = [str(card) for card in self.cards]
        return ', '.join(card_list)


    def __repr__(self):
        return self.__str__
