class Player:
    """This is the player class, it contains information about the player's
    hand and hand value.

    Responsibilities:

    * Stores Hand objects containing Card objects that the player controls
    * Keeps track of players betting money

    Collaborations:

    * Informs the game of amount of money player has remaining to wager
    """

    def __init__(self, name):
        self.name = name
        self.hands = []
        self.money = 1000

    def modify_money(self, value):
        if self.money + value > 0:
            self.money += value
        else:
            raise ValueError("Player money cannot be negative.")
