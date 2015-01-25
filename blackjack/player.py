from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand


class Player:
    """

    Responsibilities:
    * has chips
    * bets chips
    * wins chips

    Collaborators:"""

    def __init__(self, chips=100, bet=10):
        self.chips = chips
        self.bet = bet

    def make_bet(self):
        self.chips -= self.bet
        return self.chips

    def win_bet(self):
        self.chips += (2*self.bet)
        return self.chips

    def win_blackjack(self):
        self.chips += (2.5*self.bet)
        return self.chips

    def push(self):
        self.chips += self.bet
        return self.chips

    def __str__(self):
        return "Player has {} chips.".format(self.chips)

    def __repr__(self):
        return self.__str__()
