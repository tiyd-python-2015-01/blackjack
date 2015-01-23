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
    def __init__(self):
        self.money = 100
        self.hands = []
