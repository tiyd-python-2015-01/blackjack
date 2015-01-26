from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand


class Player:
    """Keeps track of the player's betting

    Responsibilities:
    * has chips
    * bets chips
    * wins chips of various values
    * holds the player's name"""

    def __init__(self, chips=100, bet=10, name='Player'):
        self.chips = chips
        self.bet = bet
        self.name = name

    def make_bet(self):
        """makes initial bet, taking bet amount from chip count"""
        self.chips -= self.bet
        return int(self.chips)

    def win_bet(self):
        """returns original bet, plus bet amount for winning"""
        self.chips += (2*self.bet)
        return int(self.chips)

    def win_blackjack(self):
        """returns original bet, plus augmented blackjack winnings"""
        self.chips += int(2.5*self.bet)
        return int(self.chips)

    def push(self):
        """returns original bet"""
        self.chips += self.bet
        return int(self.chips)

    def __str__(self):
        return "Player has {} chips.".format(self.chips)

    def __repr__(self):
        return self.__str__()
