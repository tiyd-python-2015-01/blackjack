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

    def modify_money(self, value):
        if self.money + value > 0:
            self.money += value
        else:
            raise ValueError("Player money cannot be negative.")

    def takes_hit(self, hand, card):
        hand.add_cards(card)

    def splits(self, hand, cards):
        self.modify_money(-1 * hand.bet)
        new_hand = Hand(hand.bet, [hand.cards[1], cards[0]])
        hand.cards.pop(1)
        hand.add_cards(cards[1])
        self.hands.append(new_hand)

    def doubles(self, hand, card):
        self.modify_money(-1 * hand.bet)
        hand.bet *= 2
        self.takes_hit(hand, card)

    def surrenders(self, hand):
        self.modify_money(.5 * hand.bet)
        hand.bet *= .5
