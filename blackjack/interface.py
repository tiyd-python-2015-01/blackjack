"""
Interface
    Responsibilities:
        -Accept user input
        -Output appropriate text
    Collaborators
        -Game
"""
from .player import Player
from .player import Dealer

class Interface:
    def __init__(self):
        pass

    def welcome(self):
        print("""\n\nWelcome to the game of blackjack!""")
        print("""Would you like to play a game?""")
        return self.yes_or_no()

    def display_hands(self,player,dealer):
        player_hand = ("Your hand:\n{}\n".format(player.display_hand()))
        dealer_hand = ("Dealer hand:\n{}\n".format(dealer.display_hand()))
        print(player_hand)
        print(dealer_hand)
        return "{}\n{}".format(player_hand,dealer_hand)

    def hit_or_stand(self):
        print("Another Card?")
        return self.yes_or_no()

    def play_again(self):
        print("Would you like to play again?")
        return self.yes_or_no()

    def yes_or_no(self):
        print("[Y]es")
        print("[N]o\n")
        answer = input(">>").lower()
        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            return self.yes_or_no()
