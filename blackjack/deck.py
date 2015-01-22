from blackjack.card import Card, ranks, suits
from blackjack.player_hand import Player_hand
import random

class Deck:
    """a deck of cards

    Responsibilites:

    *holds collection of cards
    *new deck shoul have all 52 cards
    *allow others to draw cards
    *shuffles cards or re-shuffle
    *report its current size

    *deals cards
    *dealer gets first card down

    Collaboraters:

    *collected from card class
    *deals cards to Hand"""


    #def __eq__(self, other):


    def __init__(self):
        self.__cards__ = [Card(rank, suit)
                         for rank in ranks
                         for suit in suits]

    def __len__(self):
        return len(self.__cards__)


    def __str__(self):
        return str(self.__card__)


    def shuffle_deck(self):
        random.shuffle(self.__cards__)
        return self.__cards__

#"""take a card from the deck and return it."""

    def deal_cards(self):
        return self.__cards__.pop()

        
        #for num in num cards:

        #player_hand.card1 = shuffled_deck.pop()
        #player_hand.card2 = shuffled_deck.pop()
        #dealer_hand.card1 = shuffled_deck.pop()
        #dealer_hand.card2 = shuffled_deck.pop()
        #print(player_hand.card1, player_hand.card2)
        #return True
        #new_deck = Deck()
        #print(type(new_deck.card_deck))

#print(Deck.deal_cards(2, Deck.huffle_deck()))
#print(Deck.shuffle_deck())
