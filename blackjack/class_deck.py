import class_card
import random


class Deck:
    """A deck of cards.

    Responsibilities:

    * Has a collection of cards
    * Shuffles cards
    * Deals out cards

    Collaborators:

    * Collected from card class.
    * Deals cards to Dealer_hand and Player_hand class """

    def __str__(self):
        return str(self.card_deck)

    def __init__(self):
        self.card_deck =[class_card.Card(rank, suit)
                         for rank in class_card.ranks
                         for suit in class_card.suits]

    def shuffle_deck():
        random.shuffle(card_deck)
        return card_deck

    def deal_card():
        return self.card_deck.pop()


fresh_deck = Deck()
print(type(fresh_deck.card_deck))

#Dealer gets 1st card down. Rest are face up.
