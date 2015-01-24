class Dealer:
    """This is the Dealer class, it contains information about the Dealer's
    hand and hand value.

    Responsibilities:

    * Stores Hand objects containing Card objects that the dealer controls
    * Determines the dealer's action based off of it's hand value

    Interactions:
    * Receives hand value information from the Hand class
    * Provides feedback about Dealer actions to the Game class
    """

    def __init__(self, hit_soft_17=False):
        self.hand = None
        self.hit_soft_17 = hit_soft_17

    def hit(self):
        """Determines if the dealer should hit or not.  Has option to allow
        for hit/no hit on soft 17"""
        if not self.hit_soft_17:
            return self.hand.get_value() < 17
        else:
            if self.hand.get_value() < 17:
                return True
            elif self.hand.get_value() == 17 and "A" in self.hand.get_ranks():
                return True
            else:
                return False

    def get_show_card(self):
        """Returns the dealer's show card for display in the game"""
        return self.hand.cards[0]

    def takes_hit(self, card):
        """Appends a dealt card to the dealer's hand"""
        self.hand.cards.append(card)
