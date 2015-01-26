from hand import Hand


class Player:
    """The player of the blackjack game.

    Responsibilities:

    * Holds a hand
    * Can bet
    * Can hit
    * Can display hand

    Collaborators:

    *Uses a hand of cards
    """
    def __init__(self, name, stack=100, hand=None):
        if hand is None:
            hand = Hand([])
        self.name = name
        self.hand = hand
        self.cards = hand.hand
        self.stack = stack

    def hit(self, deck):
        self.hand.draw(deck)

    def bet(self, amount):
        chips = self.stack
        new_chips = chips - amount
        self.stack = new_chips
        return self.stack

    def show_hand(self):
        print("{name}'s hand: "
              "{hand} ({value})".format(name=self.name,
                                        hand=self.hand,
                                        value=self.hand.best_hand))
