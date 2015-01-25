from card import Card
from deck import Deck
from player import Player
from dealer import Dealer
from interface import Interface

class Game:
    """Run the main Blackjack game loop

    Responsibilities:
    * Starts Game
    * Starts New Hand if Player has $
    * Evaluate who wins and loses
    * Pays out bets

    Collaborators:
    * Card & Deck
    * Player & Dealer
    * Interface for input & output
    """

    def __init__(self):
        self.interface = Interface()

    def game_start(self):
        self.player = Player()
        self.dealer = Dealer()


    def start_hand(self):
        self.player.bank -= 10
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player.take_a_hit(self.deck)
        self.dealer.take_a_hit(self.deck)
        self.player.take_a_hit(self.deck)
        self.dealer.take_a_hit(self.deck)
        self.interface.show_current(self.player, self.dealer)

    def blackjack_check(self):
        if self.dealer.blackjack():
            if self.player.blackjack():
                self.interface.show_final(self.player, self.dealer)
                self.player.bank += 10
                self.interface.you_push(self.player)
                self.clear_hands()
                return False#Hand is over
            else:
                self.interface.show_final(self.player, self.dealer)
                self.interface.you_lose(self.player)
                self.clear_hands()
                return False#Hand is over
        elif self.player.blackjack():
            self.interface.blackjack(self.player)
            self.player.bank += (10 * 1.5)
            self.clear_hands()
            return False#Hand is over

    def player_turn(self):##Come back and look at this to understand the logic
        while True:
            if self.interface.player_choice(self.player, self.deck):
                self.interface.show_current(self.player, self.dealer)
                return True#if player stands
            self.interface.show_current(self.player, self.dealer)
            if self.player.hand_value() > 21:
                self.interface.you_lose(self.player)
                self.clear_hands()
            return False#end hand somehow

    def dealer_turn(self):
        while True:
            self.interface.show_dealer_hand(self.dealer)
            self.interface.show_dealer_total(self.dealer)
            if self.dealer.hand_value() <= 16:
                self.dealer.take_a_hit(self.deck)
            elif self.dealer.hand_value() >= 17:
                break

    def win_loss_check(self):
        self.interface.show_final(self.player, self.dealer)
        if self.dealer.hand_value() > 21:
            self.player.bank += 20
            self.interface.you_win(self.player)
            self.clear_hands()
        elif self.dealer.hand_value() > self.player.hand_value():
            self.interface.you_lose(self.player)
            self.clear_hands()
        elif self.dealer.hand_value() == self.player.hand_value():
            self.player.bank += 10
            self.interface.you_push(self.player)
            self.clear_hands()
        else:
            self.player.bank += 20
            self.interface.you_win(self.player)
            self.clear_hands()

    def check_bank(self, player):
        if self.player.bank > 0:
            self.interface.new_hand(self.player)
        else:
            self.interface.no_money(self)
            return False#end game

    def clear_hands(self):
        del self.player.hand[:]
        del self.dealer.hand[:]

    def main_game(self):
        while True:
            self.interface.welcome_message()
            self.game_start()
            while True:
                self.start_hand()
                while True:
                    self.blackjack_check()
                    self.player_turn()
                    self.dealer_turn()
                    self.win_loss_check()
                    self.check_bank(self.player)
                    break
            break
