from blackjack.card import Card
from blackjack.deck import Deck

class Hand:
    """ The current cards in the hand

    Responsibilities:
    * keep track of which cards are in the hand
    * keep track of the value of the hand


    Collaborators:
    * get popped cards from the shoe
    * give Dealer the cards and value of the two hands
    * give user the cards and value of the two hands"""

    def __init__(self):
        self.cards = []
        self.value = 0

    def _str__(self):
        card_list = [str(card) for card in self.cards]
        return ', '.join(card_list)

    def __repr__(self):
        return self.__str__()

    def get_card(self, deck):
        card = deck.draw()
        return self.cards.append(card)

    def valuation(self):
        value_dict = {'1':1,
                      '2':2,
                      '3':3,
                      '4':4,
                      '5':5,
                      '6':6,
                      '7':7,
                      '8':8,
                      '9':9,
                      '10':10,
                      'J':10,
                      'Q':10,
                      'K':10,
                      'A':11}
        hand_ranks = [card.rank for card in self.cards]
        values = [value_dict[x] for x in hand_ranks]
        return sum(values)
