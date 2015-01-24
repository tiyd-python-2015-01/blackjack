from card import Card
from deck import Deck

class Interface:
    """The prompts for displaying of input & output

    Responsibilities:

    * Ask Player for input
    *

    Collaborators:

    * Works with Game class
    *"""

    def welcome_message(self):
        print("="*25)
        print("Welcome to Blackjack")
        start = input("Would you like to play: [Y] or [N]").upper
        if start == "Y":
            continue
        if start == "N":
            quit()

    def hit_stand(self):
        move = input(">> Would you like to [H]it or [S]tand").upper
        if move == "H":
            Player.player_hit(Deck)
        if move == "S":
            ##end player turn....Break?

    def you_win(self):
        print("YOU WIN!")

    def you_lose(self):
        print("YOU LOSE")
