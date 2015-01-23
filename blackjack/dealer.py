class Dealer:
    """The dealer is one of the two agents in the game, and plays
    deterministically against the player.

    Responsibilities:
    The dealer posesses a hand.
    The dealer will hit whenever the dealer's hand is under 17.

    Collaborators:
    The dealer posesses a hand.
    The dealer is one of the two agents in the game.
    """
    def __init__(self):
        self.hand = Hand()

    def deal(self, deck):
        self.hand.grab(deck)
        self.hand.grab(deck)

    def show_first_card(self):
        card_string = self.hand.show_cards(just_one=True)
        print "The dealer has a: {}".format(card_string)
