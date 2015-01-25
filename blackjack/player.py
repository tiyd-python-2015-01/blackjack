from card import Card
from deck import Deck

class Player:
    """The person playing the game against the Dealer(CPU)

    Responsibilities:

    * Has an active hand of dealt cards
    * Calculates the point value of hand
    * Makes decision on whether to hit or stand
    * Has starting bank of $100 and makes $10 bets

    Collaborators:

    * Recives cards from Deck class.
    *"""

    def __init__(self, hand=[], bank=100):
        self.hand = hand
        self.bank = bank


    def __len__(self):
        """Keeps up with amount of cards in hand"""
        return len(self.hand)


    def take_a_hit(self, deck):
        card = deck.deal_card()
        return self.hand.append(card)


    def hand_value(self):
        value = 0
        #aces = 0 FIGURE OUT HOW TO FLIP ACE VALUE 1 or 11
        for card in self.hand:
            if type(card.rank) == int:
                value += card.rank
            elif card.rank == "Ace":
                value += 11
            else:
                value += 10
        return value

    def blackjack(self):
        if self.hand_value() == 21 and len(self.hand) == 2:
            return True
        else:
            return False


    def __str__(self):
        """String representation of player hand as list of cards."""
        return str(self.hand)


    def __repr__(self):
        return self.__str__()
