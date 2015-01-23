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
            self.user.is_blackjack()
            self.dealer.is_blackjack()
            while not self.user.is_blackjack() and self.player_hit_or_stand():
                self.user.get_card(self.shoe.give_card())
                self.interface.show_cards(self.user)
                if self.user.busted():
                    break
            while not self.user.busted() and self.dealer.hit_or_stand():
                self.dealer.get_card(self.shoe.give_card())
                self.interface.dealer_hits(self.dealer)
                if self.dealer.busted():
                    break
            else:
                self.interface.dealer_stands(self.dealer)
            self.win_or_lost()
            if not self.interface.play_again():
                return False

    def win_or_lost(self):
        self.interface.final_cards(self.user,self.dealer)
        if self.user.busted():
            return self.player_loses(self.user)
        if self.dealer.busted():
            return self.player_wins(self.user)
        if self.user.assess_hand() > self.dealer.assess_hand():
            return self.player_wins(self.user)
        elif self.user.assess_hand() < self.dealer.assess_hand():
            return self.player_loses(self.user)
        elif self.user.assess_hand() == 21:
            if self.user.is_blackjack() and not self.dealer.is_blackjack():
                return self.player_wins(self.user)
            elif self.dealer.is_blackjack() and not self.user.is_blackjack():
                return self.player_loses(self.user)
            else:
                return self.player_ties(self.user)
        else:
            return self.player_ties(self.user)

    def player_loses(self,player):
        self.user.cash -= 10
        self.interface.player_loses(self.user)

    def player_wins(self,player):
        self.user.cash += 10
        self.interface.player_wins(self.user)

    def player_ties(self,player):
        self.interface.player_ties(self.user)

    def deal_cards(self):
        self.user.get_hand(self.shoe.deal_hand())
        self.dealer.get_hand(self.shoe.deal_hand())

    def show_cards(self):
        self.interface.display_hands(self.user, self.dealer)

    def player_hit_or_stand(self):
        return self.interface.hit_or_stand()

    def dealer_hit_or_stand(self):
        return self.interface.dealer_hit_or_stand()
