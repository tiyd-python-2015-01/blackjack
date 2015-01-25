from hand import Hand

class Dealer:
    """The dealer is one of the two agents in the game, and plays
    deterministically against the player.

    Responsibilities:
    The dealer posesses a hand.
    The dealer will hit whenever the dealer's hand is under 17.
    The dealer discards cards at the end of a round.

    Collaborators:
    The dealer posesses a hand.
    The dealer is one of the two agents in the game.
    """
    def __init__(self):
        self.hand = Hand()

    def deal(self, deck):
        self.hand.grab(deck.draw())
        self.hand.grab(deck.draw())

    def show_first_card(self):
        card_string = self.hand.show_cards(just_one=True)
        print("The dealer has a: {}".format(card_string))

    def show_cards(self):
        card_list = self.hand.show_cards()
        card_string = ", ".join(card_list)
        hand_value = self.hand.value()
        print("The dealer has: {} ({})".format(card_string, hand_value))

    def hit_from_deck(self, deck):
        self.hand.grab(deck.draw())

    def dump_cards(self):
        self.hand = Hand()

    def choose_to_hit(self):
        return self.hand.value() < 17

    def get_value(self):
        return self.hand.value()

    def is_bust(self):
        return self.hand.value() > 21

    def has_blackjack(self):
        return self.hand.is_blackjack()
