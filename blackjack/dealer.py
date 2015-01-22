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

    def __init__(self):
        self.hand = None

    def hit(self):
        if self.hand.get_value() < 17:
            return True
        else:
            return False
