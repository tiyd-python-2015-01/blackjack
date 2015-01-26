from player import Player
from dealer import Dealer
import sys

class Interface:
    """The prompts for displaying of input & output

    Responsibilities:

    * Ask Player for input
    * Displays output messages

    Collaborators:

    * Works with Game class
    *"""

    def __init__(self):
        pass

    def welcome_message(self):
        print("="*25)
        print("Its time for Blackjack")
        start = input("Would you like to play: [Y] or [N]").upper()
        if start == "Y":
            return True
        elif start == "N":
            return sys.exit()
        else:
            return self.welcome_message()


    def you_win(self, player):
        print("*"*25)
        print("\nYOU WIN!")
        print("Your new $$$ total is: ${}\n".format(player.bank))
        print("*"*25, "\n")

    def you_lose(self, player):
        print("*"*25)
        print("Bummer, you lost")
        print("Your new $$$ total is: ${}\n".format(player.bank))
        print("*"*25)

    def you_push(self, player):
        print("Game is a push")
        print("Your new $$$ total is: ${}".format(player.bank))

    def no_money(self):
        print("You're out of chips. GAME OVER")

    def blackjack(self, player):
        print("You have BLACKJACK!")
        print("Your new $$$ total is: ${}".format(player.bank))


    def show_player_hand(self, player):
        print("\nYour hand is: {}".format(player.hand))

    def show_player_total(self, player):
        print("Hand Value: {}".format(player.hand_value()))

    def show_dealer_upcard(self, dealer):
        print("Dealers up card is: {}\n".format(dealer.hand[1:]))

    def show_dealer_hand(self, dealer):
        print("\nDealer's hand is: {}".format(dealer.hand))

    def show_dealer_total(self, dealer):
        print("Dealer Value: {}\n".format(dealer.hand_value()))

    def show_current(self, player, dealer):
        self.show_player_hand(player)
        self.show_player_total(player)
        self.show_dealer_upcard(dealer)

    def show_final(self, player, dealer):
        self.show_player_hand(player)
        self.show_player_total(player)
        self.show_dealer_hand(dealer)
        self.show_dealer_total(dealer)

    def player_choice(self, player, deck):
        choice = input("Do you want to [H]it or [S]tand?").upper()
        if choice == "H":
            player.take_a_hit(deck)
            return False
        elif choice == "S":
            return True
        else:
            return self.player_choice(player, deck)

    def new_hand(self, player):
        print("="*25)
        start = input("Would you like to play a new hand? [Y] or [N]").upper()
        if start == "Y":
            return True
        elif start == "N":
            return sys.exit()
        else:
            return self.new_hand(player)
