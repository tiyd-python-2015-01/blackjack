"""
Game_State
    Responsibilities:
        -Store Table_State      -Manage the Shoe
    Collaborators:
        -Game       -Players    -Table_State
        -Shoe       -Card

"""


from .carddeckshoe import Card
from .carddeckshoe import Deck
from .carddeckshoe import Shoe


class Game_State:

    def __init__(self):
        self.cards_on_table = []
        self.shoe = Shoe()

    def add_card(new_card):
        cards.append(new_card)
