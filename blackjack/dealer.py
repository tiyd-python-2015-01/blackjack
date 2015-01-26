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
    * Display just the shown card when the dealer's hole card is
    still concealed

    Collaborators:
    * uses the Hand class to determine the value of the hand, on which it
    bases its actions"""

    def __init__(self):
        pass

    def hit_test(self, a_hand):
        """algorithm to determine the automated actions of the dealer.
        This includes the idea of the dealer hitting on a 'soft' 17"""

        value_dict = {'1': 1,
                      '2': 2,
                      '3': 3,
                      '4': 4,
                      '5': 5,
                      '6': 6,
                      '7': 7,
                      '8': 8,
                      '9': 9,
                      '10': 10,
                      'J': 10,
                      'Q': 10,
                      'K': 10,
                      'A': 11}
        hand_ranks = [card.rank for card in a_hand.cards]
        values = [value_dict[x] for x in hand_ranks]
        value = sum(values)

        list_of_a = [card.rank for card in a_hand.cards if card.rank == 'A']
        if len(list_of_a) > 0 and value < 21:
            if a_hand.value < 18:
                return "HIT"
            else:
                return "STAND"
        else:
            if a_hand.value < 17:
                return "HIT"
            else:
                return "STAND"

    def shown(self, a_hand):
        """displays just 1 card of the dealer's at the start of the hand"""
        return a_hand.cards[1]

    def shown_value(self, a_hand):
        """calculates the value of just the dealer's starting shown card"""
        card = a_hand.cards[1]
        new_hand = Hand()
        new_hand.cards = [card]
        value = new_hand.valuation()
        return value

    def __str__(self):
        return "Dealer"

    def __repr__(self):
        return self.__str__()
