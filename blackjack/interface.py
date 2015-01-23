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
        #player_hand = ("Your hand:\n{}\n".format(player.display_hand()))
        #dealer_hand = ("Dealer hand:\n{}\n".format(dealer.display_hand()))
        #print(player_hand)
        #print(dealer_hand)
        #return "{}\n{}".format(player_hand,dealer_hand)
        player_hand = player.display_hand()
        dealer_hand = dealer.display_hand()
        print("Your Hand:\t\t\t\tDealer Hand")
        print("{}\t\t\t\t{}".format(player_hand,dealer_hand))
        return "{}\n{}".format(player_hand,dealer_hand)

    def player_wins(self,player):
        print("You win!")
        self.players_pot(player)

    def player_loses(self,player):
        print("You lose.")
        self.players_pot(player)

    def player_ties(self,player):
        print("Game is a push.")
        self.players_pot(player)

    def players_pot(self,player):
        print("You currently have ${}".format(player.cash))

    def hit_or_stand(self):
        print("Another Card?")
        return self.yes_or_no()

    def show_cards(self, player):
        print("Your cards:")
        print(player.display_hand())

    def dealer_hits(self,dealer):
        print("Dealer hits")
        print(dealer.display_hand())

    def dealer_stands(self, dealer):
        print("Dealer stands")
        print(dealer.display_hand())

    def play_again(self):
        print("Would you like to play again?")
        return self.yes_or_no()

    def busted(self):
        print("You've busted.")
        print("Game over.")

    def final_cards(self,player,dealer):
        # print("Your cards")
        # print(player.display_hand())
        # print("With a value of: {}\n".format(player.assess_hand()))
        # print("Dealer's cards")
        # print(dealer.display_entire_hand())
        # print("With a value of: {}\n".format(dealer.assess_hand()))
        player_hand = player.display_hand()
        dealer_hand = dealer.display_entire_hand()
        print("Your Hand:\t\t\t\tDealer Hand")
        print("{}\t\t\t\t{}".format(player_hand,dealer_hand))
        print("Value: {}\t\t\t\tValue: {}".format(player.assess_hand(),dealer.assess_hand()))


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
