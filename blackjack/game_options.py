class GameOptions:
    """ The game options class is responsible for storing all of the rule
    variations that the player wishes to use in the game.  It contains
    boolean variables corresponding to the available rulesets.  It also
    checks to ensure that contradictory rules are not chosen.

    Responsibilities:
    * Maintains a list of rules selected by the player

    Collaborations:
    * Rules are updated by the interface
    * Rules are passed to the game during initialization
    """


    def __init__(self):
        self.number_of_decks = 1
        self.hit_on_soft_17 = False
        self.early_surrender = False
        self.resplitting = False
        self.resplit_aces = False
        self.hit_split_aces = False
        self.split_by_rank = False
        self.no_surrender = False
        self.double_9_10_11 = False
        self.double_9_10 = False
        self.no_hole_card = False
        self.no_hole_card_obo = False
