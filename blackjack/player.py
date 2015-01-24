from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.functions import checker_for_letters as cfl
class Player:
    """
    Responsibilities:
    Has a hand and can accept cards into that hand.
    Should have a way of signeling hit or stay.

    Collaborates with:
    Deck.
    """
    def __init__(self, money=100):
        self.hand = Hand()
        self.money = money



    def __str__(self):
        return "Your hand consists of {}.".format(self.hand)


    def __repr__(self):
        return self.__str__()


    def make_bet(self, amount):
        """Subtracts the amount a player bets."""
        self.money -= amount


    def get_pot(self, amount):
        """Adds money for winning a game."""
        self.money += amount



    def take_card(self, deck):
        """From the in play deck a card is drawn and the player is given a card."""
        card = deck.deal_card()
        self.hand.add(card)
        return self.hand
