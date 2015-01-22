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
