from hand import Hand
class Player:
    """This is the player class, it contains a list of hands controlled by the
    player and keeps track of how much money the player has won.

    Responsibilities:

    * Stores Hand objects containing Card objects that the player controls
    * Keeps track of players betting money

    Collaborations:

    * Informs the game of amount of money player has remaining to wager
    """

    def __init__(self, name):
        self.name = name
        self.hands = []
        self.money = 100
        self.insured = False

    def buys_insurance(self):
        """Modifys the player's money if they choose to buy insurance when
        offered"""
        self.modify_money( int(-.5*self.hands[0].bet))
        self.insured = True

    def modify_money(self, value):
        """Updates the player's money based on the supplied value.  To
        decrease money, value should be negative"""
        if self.money + value >= 0:
            self.money += value
        else:
            raise ValueError("Player money cannot be negative.")

    def takes_hit(self, hand, card):
        """Adds the supplied card to the specified hand of the player.
        Multiple hands may exist if player splits"""
        hand.add_cards(card)

    def splits(self, hand, cards):
        """Splits the player's hand into two hands, each containing one of
        the cards from the original hand, plus a newly dealt card."""
        self.modify_money(-1*hand.bet)
        new_hand = Hand(hand.bet, [hand.cards[1], cards[0]])
        hand.cards.pop(1)
        hand.add_cards(cards[1])
        self.hands.append(new_hand)

    def doubles(self, hand, card):
        """Doubles the player's bet on the current hand."""
        self.modify_money(-1*hand.bet)
        hand.bet *= 2
        self.takes_hit(hand, card)

    def surrenders(self, hand):
        """Returns half of the player's bet if they choose to surrender the
        hand."""
        self.modify_money(int(.5*hand.bet))

    def reset_player(self):
        """Resets the players list of controlled hands"""
        self.hands = []
