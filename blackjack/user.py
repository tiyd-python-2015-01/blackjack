class User:
    """User bets, hand actions, and chip count.

    Responsibilities:

    * Gives initial chip count:
        500
    * Chooses game settings:
        Change bet?
        Deal Hand

    * Gives options of bets to user:
        10
        50
        100

    Collaborators:

    * Chooses possible actions passed from Hand
    * Chooses how much to bet.
    * Game_manager class sends user double bet if wins. """

# Account for a push occurring

    def __init__(self):
        self.chip_count = 500
