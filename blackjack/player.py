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


    # def initilize_pot(self, amount):
    #     pass


    def hit(self, deck):
        """From the in play deck a card is drawn and the player is given a card."""
        card = deck.deal_card()
        self.hand.add(card)
        return self.hand


    def turn(self, deck, dealer):
        print("How much would you like to bet?")
        # Need to make some sort of bet attribute for player.
        print("What would you like to do?")
        while choice != "H" and choice !="S":
            choice = cfl("Would you like to [H]it or [S]tand?")
            if choice == "H":
                self.hand.hit(deck)
                # if check(bust):
                    # Make a you lose loop that will explain you lose and
                    # subtract the amount you bet from the
            if choice == "S":
                # Now this goes to dealers turn
                dealer.turn(deck)
