"""
Game
    Responsibilities:
        -Communicate the Game_State to Interface
        -Communicate the Interface to Game_State
        -Allow Players (Human & Dealer) to effect Game_State
        -Allow Game_State to effect Players (ie, deal cards)
        -Control game flow (ie, whose turn it is, end of game)
    Collaborators
        -Game_State
        -Interface
        -Players
"""

from .interface import Interface
from .game_state import Game_State
from .player import Player
from .carddeckshoe import Card
from .carddeckshoe import Deck
from .carddeckshoe import Shoe


class Game:

    def __init__(self):
        self.user = Player()
        self.dealer = Player()
        self.gamestate = Game_State()

    def game_loop():
        return True


if __name__ == '__main__':
    pass
