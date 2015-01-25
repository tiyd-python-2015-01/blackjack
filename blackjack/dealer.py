from card import Card
from deck import Deck

class Dealer:
    """The CPU Player playing the game human player

    Responsibilities:

    * Has an active hand of dealt cards
    * Calculates the point value of hand
    * Hit/Stands on calculated point value of hand

    Collaborators:

    * Recives cards from Deck class.
    * Interacts with Game Class
    * Interacts with Interface Class"""

    def __init__(self, hand=[]):
        self.hand = hand


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
