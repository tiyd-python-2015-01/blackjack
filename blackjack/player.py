from hand import Hand

class Player:
    """The player posesses a hand (or more, depending on the rules), and makes
    decisions to bet, to draw cards, and to stand, (among other possibilities)
    as dictated by the user.

    Responsibilities:
    Has one (or more) hands.
    Has money.
    Optionally adds cards to hands during the player's turns.

    Collaborators:
    Is one of two agents contained in the game.
    Has at least one hand.
    """
    def __init__(self, bet=10):
        self.money = 100
        self.hands = []
        self.bet = bet

    def deal(self, deck):
        hand = Hand()
        hand.grab(deck.draw())
        hand.grab(deck.draw())
        self.hands.append(hand)

    def lose_money(self):
        """When called, subtracts the bet from the player's money."""
        self.money -= self.bet

    def win_blackjack(self):
        """When called, increases the player's winnings by the special
           blackjack multipier of the bet"""
        self.money += (self.bet * 1.5)

    def win_money(self):
        """When called, increases the player's winnings by the bet."""
        self.money += self.bet

    def show_cards(self):
        your_hand = self.hands[0]
        card_string = your_hand.show_cards()
        print("You have: {}".format(card_string))

    def is_broke(self):
        return self.money <= 0

    def dump_cards(self):
        self.hands = []
