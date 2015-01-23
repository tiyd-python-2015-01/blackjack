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
from .player import Dealer
from .carddeckshoe import Card
from .carddeckshoe import Deck
from .carddeckshoe import Shoe


class Game:

    def __init__(self):
        self.user = Player()
        self.dealer = Dealer()
        self.interface = Interface()


    def start_game(self):
        if self.interface.welcome():
            return self.game_loop()
        else:
            return False

    def game_loop(self):
        self.shoe = Shoe(1)
        self.shoe.shuffle()
        while True:
            self.deal_cards()
            self.show_cards()
            while self.hit_or_stand():
                pass
                self.user.get_card(self.shoe.give_card())
                self.show_cards()

            # Allow dealer to hit or stand
            # Show Dealer's hits
            # Win or Lose
            # Adjust Money
            # Game Over?
            break
        if self.interface.play_again():
            return True
        else:
            return False


    def deal_cards(self):
        self.user.get_hand(self.shoe.deal_hand())
        self.dealer.get_hand(self.shoe.deal_hand())

    def show_cards(self):
        self.interface.display_hands(self.user, self.dealer)

    def hit_or_stand(self):
        return self.interface.hit_or_stand()
