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
        player_hand = player.display_hand()
        dealer_hand = dealer.display_hand()
        max_length = max(len(player_hand),len(dealer_hand))
        print("Your Hand:".ljust(30),"Dealer Hand".ljust(30))
        for n in range(0,max_length):
            try:
                print(str(player_hand[n]).ljust(30),str(dealer_hand[n]).ljust(30))
            except:
                try:
                    print(str(player_hand[n]).ljust(30))
                except:
                    print(" ".ljust(30),str(dealer_hand[n]).ljust(60))
        print("Your Value: {}".format(player.assess_hand()).ljust(30),"\n")

        return "{}\n{}".format(player_hand,dealer_hand)

    def player_wins(self,player):
        print("You win!","\n")
        self.players_pot(player)

    def player_loses(self,player):
        print("You lose.","\n")
        self.players_pot(player)

    def player_ties(self,player):
        print("Game is a push.","\n")
        self.players_pot(player)

    def players_pot(self,player):
        print("You currently have ${}".format(player.cash),"\n")

    def hit_or_stand(self):
        print("Another Card?")
        return self.yes_or_no()

    def show_cards(self, player):
        print("Your cards:")
        cards = player.display_hand()
        for n in range(0,len(cards)-1):
            print(str(cards[n]).ljust(30))
        print("Your Value: {}".format(player.assess_hand()).ljust(30),"\n")

    def dealer_hits(self,dealer):
        print(" ".ljust(30),"Dealer hits:")
        cards = dealer.display_hand()
        for n in range(0,len(cards)):
            print(" ".ljust(30), str(cards[n]).ljust(30))
        print("")

    def dealer_stands(self, dealer):
        print(" ".ljust(30),"Dealer stands")
        cards = dealer.display_hand()
        for n in range(0,len(cards)-1):
            print(" ".ljust(30), str(cards[n]).ljust(30))
        print("")

    def play_again(self):
        print("Would you like to play again?")
        return self.yes_or_no()

    def busted(self):
        print("You've busted.")
        print("Game over.\n")

    def final_cards(self,player,dealer):
        player_hand = player.display_hand()
        dealer_hand = dealer.display_entire_hand()
        max_length = max(len(player_hand),len(dealer_hand))
        print("Your Hand:".ljust(30),"Dealer Hand".ljust(30))
        for n in range(0,max_length):
            try:
                print(str(player_hand[n]).ljust(30),str(dealer_hand[n]).ljust(30))
            except:
                try:
                    print(str(player_hand[n]).ljust(30))
                except:
                    print(" ".ljust(30),str(dealer_hand[n]).ljust(60))
        print(("Your Value: {}".format(player.assess_hand()).ljust(30)),
              ("Dealer Value: {}".format(dealer.assess_hand()).ljust(30)),"\n")
        return "{}\n{}".format(player_hand,dealer_hand)

    def farewell(self,player):
        print("Thanks for playing!")
        print("You're leaving with ${}".format(player.cash))
        
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
