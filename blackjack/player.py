"""
Player
    Responsibilities:
        -Name   -Hand   -Makes choices each turn?
    Collaborators
        -Game   -Hand   -Game_State

Dealer
    Responsibilities:
        -Stores Hand    -Plays by set of rules
    Collaborators
        -Hand   -Player     -Game

Human_Player
    Responsibilities:
        -Stores Hand    -Plays according to user input
    Collaborators
        -Hand   -Player     -Game
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.potential_values = []


class Hand:
    def __init__(self):
        self.cards = []
        self.potential_values = []
