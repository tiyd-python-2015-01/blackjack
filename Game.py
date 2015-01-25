from dealer import Dealer
from player import Player
from hand import Hand
from card import Card
from shoe import Shoe, Clubs, Diamonds, Hearts, Spades


class Game:
    """Information about the game.

    Responsibilities:

    * Check for winner
    * Handles betting and bankroll
    * Resets the game and hands

    Collaborators

    * Checks the player and dealer's hand amounts and compares them
    """

    def __init__(self, dealer, player, shoe):
        self.dealer = dealer
        self.player = player
        self.shoe = shoe
        self.pot = 0

    def play_again(self):
        choice = input('Press "p" to play again or "q" to quit: ').lower()
        return choice == 'p'


    def hit_or_stand_with_surrender_and_double(self):
        choice = input('[H]it, [S]tand, [D]ouble, or S[u]rrender: ').lower()
        if (choice == 'h') or (choice == 's') or (choice =='d') or (choice == 'u'):
            return choice
        else:
            print("Invalid input!")
            return self.hit_or_stand()

    def hit_or_stand(self):
        choice = input('[H]it, [S]tand: ').lower()
        if (choice == 'h') or (choice == 's'):
            return choice
        else:
            print("Invalid input!")
            return self.hit_or_stand()


    def check_for_winner(self, dealer, player):
        if self.player.hand.best_hand < self.dealer.hand.best_hand:
            print("You Lose")
        elif self.dealer.hand.best_hand < self.player.hand.best_hand:
            print("You Win!")
            self.player.stack += self.pot * 2
        elif self.dealer.hand.best_hand == self.player.hand.best_hand:
            print("Push!")
            self.player.stack += self.pot

    def new_turn(self):
        self.dealer.hand.reset_hand()
        self.player.hand.reset_hand()
        self.dealer.hand.new_hand(self.shoe)
        self.player.hand.new_hand(self.shoe)
        self.pot = 0


    def place_bet(self, amount):
        try:
            int(amount)
            if int(amount) <= self.player.stack:
                self.player.stack -= int(amount)
                self.pot += int(amount)
                return amount
            else:
                self.place_bet(input("Not enough funds! You have {} dollars. "
                                     "Place a bet: ".format(self.player.stack)))
        except ValueError:
            self.place_bet(input("Place a bet: "))
