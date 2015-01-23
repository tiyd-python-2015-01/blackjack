from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player

class Dealer:
    """A computer player that uses an algorithm to determine whether to hit
    or stay

    Responsibilities:
    * Stay on 17 (with no Ace in hand)
    * Hit on 17 (with Ace in hand)
    * Hit on 16 or under
    * Stay on 18-21

    Collaborators:
    * on hit, tell dealer's Hand to get Card from Shoe
    * """

    def __init__(self):
        pass


    def hit_test(self, a_hand):
        list_of_a = [card.rank for card in a_hand.cards if card.rank == 'A']
        print("Length = {}".format(len(list_of_a)))
        print("Value = {}".format(a_hand.value))
        if len(list_of_a) > 0:
            if a_hand.value < 18:
                return "Hit"
            else:
                return "Stand"
        else:
            if a_hand.value < 17:
                return "Hit"
            else:
                return "Stand"



    def shown(self, a_hand):
        return a_hand.cards[1]

    def __str__(self):
        return "Dealer"

    def __repr__(self):
        return self.__str__()
